from antlr4 import *
import sys
import os

# Add the generated files directory to Python path
DIR = os.path.dirname(__file__)
CPL_Dest = os.path.join(DIR, 'CompiledFiles_poem_ppl')
sys.path.append(CPL_Dest)

# Add the project root directory to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(DIR))  # Go up two levels from PPL to project root
sys.path.append(PROJECT_ROOT)

from PoemDSLLexer import PoemDSLLexer
from PoemDSLParser import PoemDSLParser
from PoemDSLVisitor import PoemDSLVisitor
from src.ailamtho import PoemGenerator, ControlledPoemGenerator  # Import both generators

# Define topic descriptions
TOPIC_DESCRIPTIONS = {
    0: "Gia Đình - Những bài thơ về tình cảm gia đình, cha mẹ, con cái",
    1: "Tình Yêu - Những bài thơ về tình yêu, tình cảm lứa đôi",
    2: "Dịch Bệnh - Những bài thơ về đại dịch, sức khỏe, y tế",
    3: "Quê Hương - Những bài thơ về quê hương, đất nước, quốc gia",
    4: "Lễ Tết - Những bài thơ về ngày lễ, tết, truyền thống"
}

class PoemDSLVisitorImpl(PoemDSLVisitor):
    def __init__(self):
        self.result = None
        self.error = None

    def visitCommand(self, ctx):
        return self.visitChildren(ctx)

    def visitGeneratePoem(self, ctx):
        try:
            model_id = int(ctx.INT(0).getText())
            context = ctx.STRING().getText().strip('"')
            n_stanzas = int(ctx.INT(1).getText())

            # Validate parameters
            if model_id < 0:
                raise ValueError("Model ID must be non-negative")
            if n_stanzas <= 0:
                raise ValueError("Number of stanzas must be positive")

            # Generate poem
            generator = PoemGenerator(model_id=model_id)
            poem = generator.generate_poem(context=context, n_stanzas=n_stanzas)
            self.result = poem

        except Exception as e:
            self.error = str(e)

    def visitGenerateControlledPoem(self, ctx):
        try:
            context = ctx.STRING().getText().strip('"')
            topic_id = int(ctx.INT().getText())

            # Validate topic_id
            if not 0 <= topic_id <= 4:
                raise ValueError("Topic ID must be between 0 and 4")

            # Generate controlled poem using ControlledPoemGenerator
            generator = ControlledPoemGenerator()
            poem = generator.generate_poem(context=context, topic_id=topic_id)
            self.result = poem

        except Exception as e:
            self.error = str(e)

    def visitHelpCommand(self, ctx):
        help_text = """
Các lệnh có sẵn:

1. Tạo thơ thông thường:
   GENERATE POEM MODEL <model_id> CONTEXT "<text>" STANZAS <number>
   hoặc
   GEN POEM M <model_id> C "<text>" S <number>

2. Tạo thơ có chủ đề:
   GENERATE CONTROLLED POEM CONTEXT "<text>" TOPIC <topic_id>
   hoặc
   GEN CONTROLLED POEM C "<text>" T <topic_id>

3. Xem danh sách chủ đề:
   LIST TOPICS
   hoặc
   SHOW TOPICS

4. Xem thông tin model:
   SHOW MODEL INFO

5. Xem hướng dẫn:
   HELP
   hoặc
   SHOW COMMANDS

Trong đó:
- <model_id>: số nguyên >= 0
- <text>: chuỗi ký tự tiếng Việt, có thể có dấu
- <number>: số nguyên > 0
- <topic_id>: số nguyên trong khoảng 0-4
"""
        self.result = help_text

    def visitListTopics(self, ctx):
        topics_text = "Danh sách các chủ đề có sẵn:\n\n"
        for topic_id, description in TOPIC_DESCRIPTIONS.items():
            topics_text += f"{topic_id}: {description}\n"
        self.result = topics_text

    def visitShowModelInfo(self, ctx):
        model_info = """
Thông tin về các model:

1. Model thông thường (PoemGenerator):
   - Sinh thơ dựa trên context và số khổ
   - Không giới hạn chủ đề
   - Có thể chọn model_id khác nhau

2. Model có chủ đề (ControlledPoemGenerator):
   - Sinh thơ theo chủ đề cụ thể
   - 5 chủ đề có sẵn:
     + 0: Gia Đình
     + 1: Tình Yêu
     + 2: Dịch Bệnh
     + 3: Quê Hương
     + 4: Lễ Tết
   - Tối ưu cho từng chủ đề
"""
        self.result = model_info

def parse_poem_command(command: str) -> tuple[bool, str]:
    """
    Parse a poem generation command and return (success, result/error_message)
    """
    try:
        # Create lexer and parser
        input_stream = InputStream(command)
        lexer = PoemDSLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PoemDSLParser(token_stream)

        # Parse the command
        tree = parser.command()

        # Visit the parse tree
        visitor = PoemDSLVisitorImpl()
        visitor.visit(tree)

        if visitor.error:
            return False, f"Error: {visitor.error}"
        return True, visitor.result

    except Exception as e:
        return False, f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test commands
    test_commands = [
        'GENERATE POEM MODEL 0 CONTEXT "ai ơi" STANZAS 2',
        'GEN POEM M 0 C "ai ơi" S 2',
        'GENERATE CONTROLLED POEM CONTEXT "cha mẹ một nắng hai sương" TOPIC 3',
        'GEN CONTROLLED POEM C "cha mẹ một nắng hai sương" T 3',
        'HELP',
        'LIST TOPICS',
        'SHOW MODEL INFO'
    ]

    for cmd in test_commands:
        print(f"\nTesting command: {cmd}")
        success, result = parse_poem_command(cmd)
        if success:
            print("Success!")
            print(result)
        else:
            print(result) 