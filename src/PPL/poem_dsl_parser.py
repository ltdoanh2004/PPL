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
        'GEN CONTROLLED POEM C "cha mẹ một nắng hai sương" T 3'
    ]

    for cmd in test_commands:
        print(f"\nTesting command: {cmd}")
        success, result = parse_poem_command(cmd)
        if success:
            print("Success!")
            print(result)
        else:
            print(result) 