
import SyntaxAnalyzer.Input as Input
from .Grammar import Grammar
from .Parser import Parser


def analyze(grammar_file_name, labels):
    procution_rules,start_symbol = Input.read_input(grammar_file_name)
    grammar_instance  = Grammar(procution_rules,start_symbol)
    print("\n\n")
    parser_instance = Parser(grammar_instance)
    parser_instance.build()
    parser_instance.add_sync_to_table()
    parser_instance.print_table()
    print("\n\n")
    parser_instance.parse_input(labels)
