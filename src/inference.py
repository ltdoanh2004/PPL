from model.poem_model import PoemModel
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate a poem')
    parser.add_argument('--model_name', type=str, default='thangduong0509/gpt2_viet_poem_generation',
                      help='Name or path of the pretrained model to use')
    parser.add_argument('--prompt', type=str, default='Tôi yêu bạn')
    args = parser.parse_args()
    poem_model = PoemModel(model_name = args.model_name)
    poem = poem_model.generate_poem(args.prompt)
    poem_model.print_poem(poem)

if __name__ == "__main__":
    main()