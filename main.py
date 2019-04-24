from tokenizer.tokenizer import get_tokens

if __name__ == '__main__':
    tokens = get_tokens("grammar.txt", "input.txt", print_tokens=True)
