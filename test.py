
from src.ailamtho import ControlledPoemGenerator
generator = ControlledPoemGenerator()
context_input = 'cha mẹ một nắng hai sương'
poem = generator.generate_poem(context=context_input, topic_id=0)
print('doanh')
print(poem)