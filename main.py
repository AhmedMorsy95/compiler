from tokenizer.getInput import read_input
from tokenizer.NFA import definitions_to_nfa
import tokenizer.tokenizer as tokenizer
from tokenizer.dfaState import state
from tokenizer.min_state import min_state
from tokenizer.RegexConverter import regexConverter
from tokenizer.node import Node
from tokenizer.graph import Graph
import tokenizer.NFA as NFA
import tokenizer.DFA as DFA
import tokenizer.minimization as minimization
from string import ascii_letters
from tokenizer.NodeGenerator import  NodeGenerator

if __name__ == '__main__':

    #
    keywords_list, punc_list, definitions_dict, expressions_dict = read_input("grammar.txt")
    # keywods_list is a list of strings containg the keywords
    # punc_list is a list of strings containg the punctuation symbols
    # definitions_dict is a dictionary, the key (string) is the definition name, and the value is the regex string that represents the definition
    # expressions_dict is a dictionary, the key (string) is the expression name, and the value is the regex string that represents the expression

    definitions_nfas = definitions_to_nfa(definitions_dict)
    # definitions_nfas is a dictionary, the key (string) is the definition name, and the value is the corresponding NFA of that definition (Graph object)

    regex = []
    for i in keywords_list:
        regex.append((i.replace(" ", ""), i))

    for i in punc_list:
        regex.append((i.replace(" ", ""),  i))

    for key, values in expressions_dict.items():
        regex.append((values.replace(" ", ""), key))

    # regex = [("(abc)*", "alpha"), ("123", "numerical")]
    #1. convert regex into nfa
    priority = {}
    sum = 0
    for i in regex:
        priority[i[1]] = sum
        sum += 1

    nfas = NFA.convert_regex_to_nfa(regex, definitions_nfas)
    #2. combine nfas together
    combined = NFA.combine_nfas(nfas)

    #3. convert nfa to dfa
    dfa = DFA.nfa_to_dfa(combined)
    print(len(state.state_instances))

    #4. minimize dfa
    # minimization.minimization_states();
    print(len(min_state.class_instance))

    #5. tokenization
    with open("input.txt", 'r') as file:
        file_lines = file.readlines()
        file.close()
    i = 0
    for line in file_lines:
        print("Line " + str(i + 1) + ':')
        tokenizer.tokenize(dfa,line,priority)
        print('\n')
        i += 1
