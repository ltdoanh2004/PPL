import pandas as pd
from datasets import Dataset
from transformers import pipeline
class PoemDataset:
    def __init__(self, dataset_path = 'poem_dataset.csv'):
        self.poem_dataset = pd.read_csv(dataset_path)
        
    def preprocess(self):
        self.poem_dataset['content'] = self.poem_dataset['content'].apply(self.split_content)
        self.poem_dataset = self.explode_content()
        self.poem_dataset = self.to_dataset()
        self.poem_dataset = self.train_test_split()
        return self.poem_dataset
    def split_content(self, content):
        samples = []
        poem_parts = content.split('\n\n')
        for poem_part in poem_parts:
            poem_in_lines = poem_part.split('\n')
            if len(poem_in_lines) == 4:
                samples.append(poem_in_lines)
        return samples
    def explode_content(self):
        self.poem_dataset = self.poem_dataset.explode('content')
        self.poem_dataset.reset_index(drop=True, inplace=True)
        self.poem_dataset = self.poem_dataset.dropna(subset=['content'])
        self.poem_dataset['content'] = self.poem_dataset['content'].apply(lambda x: '\n'.join(x))
        return self.poem_dataset

    def to_dataset(self):
        self.poem_dataset = Dataset.from_pandas(self.poem_dataset)
        return self.poem_dataset
    
    def train_test_split(self, train_size = 0.9, test_size = 0.1):
        self.poem_dataset = self.poem_dataset.train_test_split(train_size=train_size, test_size=test_size)
        return self.poem_dataset
    
    def get_train_dataset(self):
        return self.poem_dataset['train']
    
    def get_test_dataset(self):
        return self.poem_dataset['test']
    
    def get_poem_dataset(self):
        return self.poem_dataset