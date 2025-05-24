from model.poem_model import PoemModel


def main():
    poem_model = PoemModel()
    poem_model.tokenize_poem()

if __name__ == "__main__":
    main()