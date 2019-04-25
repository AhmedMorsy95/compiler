from Tokenizer.tokenizer import get_tokens
from SyntaxAnalyzer.analyzer import analyze

if __name__ == '__main__':
    tokens = get_tokens("language_grammar.txt", "input_code.txt", print_tokens=True)
    labels = [token.label for token in tokens]
    analyze("code_grammar.txt", labels)
