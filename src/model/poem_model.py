import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


class PoemModel:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained('NlpHUST/gpt2-vietnamese')
        self.model = GPT2LMHeadModel.from_pretrained('NlpHUST/gpt2-vietnamese')
        self.MAX_SEQ_LEN = 100
        self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate_poem(self, prompt, max_length = 120, min_length = 50, top_k = 40, num_beams = 5, no_repeat_ngram_size = 2, num_return_sequences = 3):
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        outputs = self.model.generate(input_ids,
                                    pad_token_id=self.tokenizer.eos_token_id,
                                    do_sample=True,
                                    max_length=max_length,
                                    min_length=min_length,
                                    top_k=top_k,
                                    num_beams=num_beams,
                                    early_stopping=True,
                                    no_repeat_ngram_size=no_repeat_ngram_size,
                                    num_return_sequences=num_return_sequences)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    


    def preprocess_function(self, row):
        return self.tokenizer(
            row['content'],
            max_length=self.MAX_SEQ_LEN,
            padding='max_length',
            truncation=True
        )
    def tokenize_poem(self, poem_dataset):
        tokenized_poem_dataset = poem_dataset.map(
        self.preprocess_function,
        batched=True,
        num_proc=4,
        remove_columns=poem_dataset['train'].column_names,
        )
        return tokenized_poem_dataset