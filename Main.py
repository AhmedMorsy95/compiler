
import Input
from Grammar import Grammar
from Parser import Parser


if __name__ == '__main__':
    file_name = "input.txt"
    procution_rules,start_symbol = Input.read_input(file_name)
    grammar_instance  = Grammar(procution_rules,start_symbol)
    print(grammar_instance.is_terminal("IF"))
    parser_instance = Parser(grammar_instance)
    # parser_instance.build()
