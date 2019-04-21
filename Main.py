
import Input
from Grammar import Grammar
from Parser import Parser


if __name__ == '__main__':

    file_name = "input.txt"
    procution_rules,start_symbol = Input.read_input(file_name)
    grammar_instance  = Grammar(procution_rules,start_symbol)
    parser_instance = Parser(grammar_instance)
    parser_instance.build()
    parser_instance.print_table()