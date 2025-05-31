import torch
from transformers import RobertaTokenizer, GPT2Config, GPT2LMHeadModel, PhobertTokenizer
from underthesea import word_tokenize

from .generate_poem import generate_text
from .generate_topic import generate_text_pplm

from src.ailamtho.utils import Config, download, post_process
from src.ailamtho.utils import get_bag_of_words_indices, build_bows_one_hot_vectors


class PoemGenerator:
    """
    A simple generator class that generates poem with some words input

    Attributes
    ----------
    model_id : int
        0: Word-Level-GPT2Model
        1: Syllable-Level-GPT2Model
        2: Custom-loss-Model

    Methods
    -------
    generate_poem(context: str, n_stanzas)
        Generate poem with some words input
    """
    def __init__(self, model_id: int):
        """
        Parameters
        ----------
        model_id : int
            0: Word Level GPT2Model
            1: Syllable Level GPT2Model
            2: Our Custom Loss Model
        """

        if model_id not in [0, 1, 2]:
            raise ValueError('model id must be in [0, 1, 2]')

        self.model_id = model_id
        self.cfg = Config.load_config()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        if self.model_id == 0:

            self.n_tokens_per_stanza = 30
            self.seg_word = True
            self.config_model = GPT2Config.from_json_file(download(self.cfg['word_level_gpt2model']['config']))
            merges_file = download(self.cfg['word_level_gpt2model']['tokenizer']['merges_file'])
            vocab_file = download(self.cfg['word_level_gpt2model']['tokenizer']['vocabs_file'])

            self.tokenizer = PhobertTokenizer(vocab_file, merges_file)
            self.tokenizer.add_tokens('\n')

            self.model = GPT2LMHeadModel(config=self.config_model)
            # self.model.load_state_dict(torch.load(download(self.cfg['word_level_gpt2model']['weight'])))
            state_dict = torch.load(download(self.cfg['word_level_gpt2model']['weight']), map_location=self.device)

            model_state_dict = self.model.state_dict()

            # Lọc bỏ những key không nằm trong model hiện tại
            filtered_state_dict = {k: v for k, v in state_dict.items() if k in model_state_dict}

            model_state_dict.update(filtered_state_dict)
            self.model.load_state_dict(model_state_dict)
            self.model.to(self.device)
            self.model.eval()

        elif self.model_id == 1:

            self.n_tokens_per_stanza = 40
            self.seg_word = False
            self.config_model = GPT2Config.from_json_file(download(self.cfg['syllable_level_gpt2model']['config']))
            merges_file = download(self.cfg['syllable_level_gpt2model']['tokenizer']['merges_file'])
            vocab_file = download(self.cfg['syllable_level_gpt2model']['tokenizer']['vocabs_file'])

            self.tokenizer = RobertaTokenizer(vocab_file, merges_file)
            self.tokenizer.add_tokens('\n')

            self.model = GPT2LMHeadModel(config=self.config_model)
            self.model.load_state_dict(torch.load(download(self.cfg['syllable_level_gpt2model']['weight'])))
            self.model.to(self.device)
            self.model.eval()

        else:

            self.n_tokens_per_stanza = 40
            self.seg_word = False
            merges_file = download(self.cfg['custom_loss_model']['tokenizer']['merges_file'])
            vocab_file = download(self.cfg['custom_loss_model']['tokenizer']['vocabs_file'])

            self.tokenizer = RobertaTokenizer(vocab_file, merges_file)
            self.tokenizer.add_tokens('\n')

            self.config_model = GPT2Config(vocab_size=self.tokenizer.vocab_size + 1, n_layer=6)

            self.model = GPT2LMHeadModel(config=self.config_model)
            self.model.load_state_dict(torch.load(download(self.cfg['custom_loss_model']['weight']))['state_dict'])
            self.model.to(self.device)
            self.model.eval()

    def generate_poem(self, context: str, n_stanzas=2):
        print(f"Input context: {context}")
        length = n_stanzas * self.n_tokens_per_stanza
        norm_text = context.strip('\n ').lower()
        if self.seg_word:
            norm_text = word_tokenize(norm_text, format='text')
        print(f"Normalized text: {norm_text}")

        print("Starting text generation...")
        text: str = generate_text(self.model, self.tokenizer, context=norm_text, device=self.device, length=length,
                                  temperature=0.85, top_k=20, sample=True, show_time=False)
        print(f"Generated text: {text}")
        
        poem = post_process(text, n_stanzas=n_stanzas)
        print(f"Final poem: {poem}")

        return poem


class ControlledPoemGenerator:
    """A class that generate poem towards the desired topic"""

    def __init__(self):

        self.id2topic = {0: 'gia_dinh', 1: 'tinh_yeu', 2: 'dich_benh', 3: 'que_huong', 4: 'le_tet'}
        self.cfg = Config.load_config()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.config_model = GPT2Config.from_json_file(download(self.cfg['word_level_gpt2model']['config']))
        merges_file = download(self.cfg['word_level_gpt2model']['tokenizer']['merges_file'])
        vocab_file = download(self.cfg['word_level_gpt2model']['tokenizer']['vocabs_file'])

        self.tokenizer = PhobertTokenizer(vocab_file, merges_file)
        self.tokenizer.add_tokens('\n')

        self.model = GPT2LMHeadModel(config=self.config_model)
        # self.model.load_state_dict(torch.load(download(self.cfg['word_level_gpt2model']['weight'])))
        state_dict = torch.load(download(self.cfg['word_level_gpt2model']['weight']), map_location=self.device)

        model_state_dict = self.model.state_dict()

        filtered_state_dict = {k: v for k, v in state_dict.items() if k in model_state_dict}

        model_state_dict.update(filtered_state_dict)
        msg = self.model.load_state_dict(model_state_dict)
        print(msg)
        self.model.to(self.device)
        self.model.eval()

        # Freeze layer
        for param in self.model.parameters():
            param.requires_grad = False

        # Reconstruct one hot vector matrix of bows
        self.one_hot_bow_vector_list = []

        for idx in range(5):
            bow_ids = get_bag_of_words_indices(download(self.cfg['bow'][self.id2topic[idx]]), tokenizer=self.tokenizer)
            one_hot_bow_vector = build_bows_one_hot_vectors(bow_indices=bow_ids, device=self.device,
                                                            tokenizer=self.tokenizer)

            self.one_hot_bow_vector_list.append(one_hot_bow_vector)

    def generate_poem(self, context, topic_id: int, max_length=30):
        print(f"Starting poem generation with context: {context} and topic_id: {topic_id}")
        
        if topic_id not in [0, 1, 2, 3, 4]:
            raise ValueError('Topic Id must be in [0, 1, 2, 3, 4]')
            
        print("Normalizing text...")
        norm_text = context.strip('\n ').lower()
        norm_text = word_tokenize(norm_text, format='text')
        print(f"Normalized text: {norm_text}")
        
        print("Checking model and tokenizer...")
        print(f"Model device: {self.model.device}")
        print(f"Model type: {type(self.model)}")
        print(f"Tokenizer type: {type(self.tokenizer)}")
        
        print("Starting text generation with PPLM...")
        try:
            # Calculate appropriate length based on desired stanzas
            target_length = max_length * 4  # 4 lines per stanza
            
            generated_text:str = generate_text_pplm(
                self.model, 
                self.tokenizer, 
                context=norm_text, 
                device=self.device,
                one_hot_bows_vectors=self.one_hot_bow_vector_list[topic_id], 
                length=target_length,
                loss_type=1, 
                window_length=7, 
                verbose=True,
                num_iterations=3,
                temperature=0.7,
                top_k=50,
                gm_scale=0.95,
                kl_scale=0.02,
                sample=True
            )
            print(f"Generated text: {generated_text}")
            
            # Process the text to count actual lines
            lines = [line.strip() for line in generated_text.split('\n')]
            lines = [line for line in lines if line and not line.isspace()]
            n_stanzas = max(1, len(lines) // 4)  # Ensure at least 1 stanza
            print(f"Number of stanzas detected: {n_stanzas}")
            
            poem = post_process(text=generated_text, n_stanzas=n_stanzas)
            print(f"Final poem after post-processing: {poem}")
            
            if not poem.strip():
                print("Warning: Generated poem is empty, trying with default stanza count")
                poem = post_process(text=generated_text, n_stanzas=2)
            
            return poem
        except Exception as e:
            print(f"Error during poem generation: {str(e)}")
            raise