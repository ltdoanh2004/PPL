from src.ailamtho import PoemGenerator
# Please specify model_id
generator = PoemGenerator(model_id=0)
context_input = 'ai ơi'
poem = generator.generate_poem(context=context_input, n_stanzas=2)
print(poem)

from src.ailamtho import ControlledPoemGenerator
generator = ControlledPoemGenerator()
context_input = 'cha mẹ một nắng hai sương'
poem = generator.generate_poem(context=context_input, topic_id=0)
print('doanh')
print(poem)