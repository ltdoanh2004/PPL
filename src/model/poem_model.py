from transformers import pipeline

class PoemModel:
    def __init__(self, model_name = 'thangduong0509/gpt2_viet_poem_generation'):
        self.generator = pipeline('text-generation', model=model_name)

    def generate_poem(self, prompt, max_new_tokens = 50, do_sample = True, top_k = 50, top_p = 0.95, temperature = 0.8, repetition_penalty = 1.2):
        results = self.generator(
            prompt,
            max_new_tokens=max_new_tokens,
            do_sample=do_sample,
            top_k=top_k,
            top_p=top_p,
            temperature=temperature,
            repetition_penalty=repetition_penalty
        )
        return results[0]['generated_text']
    def print_poem(self, poem):
        for line in poem.split('\n'):
            print(line)