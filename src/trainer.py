import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import TrainingArguments, DataCollatorForLanguageModeling
from data.dataset import PoemDataset
from transformers import Trainer
import argparse

class Trainer:
    def __init__(self, model_name = 'NlpHUST/gpt2-vietnamese', dataset_path = 'poem_dataset.csv'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.data_collator = DataCollatorForLanguageModeling(tokenizer=self.tokenizer, mlm=False)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.MAX_SEQ_LEN = 120
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.poem_dataset = PoemDataset(dataset_path)
        self.poem_dataset = self.poem_dataset.preprocess()
        self.tokenized_poem_dataset = self.tokenize_poem(self.poem_dataset)
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
    def get_trainning_args(self):
        training_args = TrainingArguments(
            output_dir='gpt2_viet_poem_generation',
            save_strategy='epoch',
            learning_rate=2e-5,
            num_train_epochs=10,
            weight_decay=0.01,
            fp16=True,
            push_to_hub=True
        )
        return training_args
    def train_model(self):
        trainer = Trainer(
            model=self.model,
            args=self.get_trainning_args(),
            train_dataset=self.tokenized_poem_dataset['train'],
            eval_dataset=self.tokenized_poem_dataset['test'],
            data_collator=self.data_collator,
            tokenizer=self.tokenizer
        )
        trainer.train()

def main():
    parser = argparse.ArgumentParser(description='Train a Vietnamese poem generation model')
    parser.add_argument('--model_name', type=str, default='NlpHUST/gpt2-vietnamese',
                      help='Name or path of the pretrained model to use')
    parser.add_argument('--dataset_path', type=str, default='poem_dataset.csv',
                      help='Path to the poem dataset CSV file')
    
    args = parser.parse_args()
    
    trainer = Trainer(model_name=args.model_name, dataset_path=args.dataset_path)
    trainer.train_model()

if __name__ == "__main__":
    main()