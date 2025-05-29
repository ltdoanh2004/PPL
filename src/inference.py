from model.poem_model import PoemModel
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate a Vietnamese poem')
    parser.add_argument('--model_name', type=str, default='thangduong0509/gpt2_viet_poem_generation',
                      help='Name or path of the pretrained model to use')
    parser.add_argument('--prompt', type=str, default='Tôi yêu bạn',
                      help='Prompt text to generate poem from')
    parser.add_argument('--max_new_tokens', type=int, default=50,
                      help='Maximum number of new tokens to generate')
    parser.add_argument('--do_sample', action='store_true', default=True,
                      help='Whether to use sampling for generation')
    parser.add_argument('--top_k', type=int, default=50,
                      help='Top k for sampling')
    parser.add_argument('--top_p', type=float, default=0.95,
                      help='Top p for sampling')
    parser.add_argument('--temperature', type=float, default=0.8,
                      help='Temperature for sampling')
    parser.add_argument('--repetition_penalty', type=float, default=1.2,
                      help='Repetition penalty for generation')
    
    args = parser.parse_args()
    
    poem_model = PoemModel(model_name=args.model_name)
    poem = poem_model.generate_poem(
        prompt=args.prompt,
        max_new_tokens=args.max_new_tokens,
        do_sample=args.do_sample,
        top_k=args.top_k,
        top_p=args.top_p,
        temperature=args.temperature,
        repetition_penalty=args.repetition_penalty
    )
    poem_model.print_poem(poem)

if __name__ == "__main__":
    main()