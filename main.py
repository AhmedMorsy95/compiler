from getInput import read_input
from NFA import definitions_to_nfa
import tokenizer
from dfaState import state
from RegexConverter import regexConverter
from node import Node
from graph import Graph
import NFA
import DFA
from string import ascii_letters

from NodeGenerator import  NodeGenerator


def go(regex, definitions):
    # regex = [("(abc)*", "alpha"), ("123", "numerical")]
    #1. convert regex into nfa
    priority = {}
    sum = 0
    for i in regex:
        priority[i[1]] = sum
        sum += 1

    nfas = NFA.convert_regex_to_nfa(regex, definitions)
    #2. combine nfas together
    combined = NFA.combine_nfas(nfas)
    #3. convert nfa to dfa
    dfa = DFA.nfa_to_dfa(combined)
    #dfa.dfs_state()
    #4. minimize dfa

    #5. tokenization
    # "int sum,count,pass,mnt;while(pass != 10){pass=pass+1;}"
    #table = DFA.build_transition_table()
    #DFA.print_transition_table(table)
    # tokenizer.tokenize(dfa,"1",priority)
    tokenizer.tokenize(dfa,"int abc123,count,pass,mnt;while(pass != 10){pass=pass+1;}",priority)

if __name__ == '__main__':

    #
    keywords_list, punc_list, definitions_dict, expressions_dict = read_input("grammar.txt")
    # keywods_list is a list of strings containg the keywords
    # punc_list is a list of strings containg the punctuation symbols
    # definitions_dict is a dictionary, the key (string) is the definition name, and the value is the regex string that represents the definition
    # expressions_dict is a dictionary, the key (string) is the expression name, and the value is the regex string that represents the expression

    definitions_nfas = definitions_to_nfa(definitions_dict)
    # definitions_nfas is a dictionary, the key (string) is the definition name, and the value is the corresponding NFA of that definition (Graph object)

    regex_all = []
    for i in keywords_list:
        regex_all.append((i.replace(" ", ""), i))

    for i in punc_list:
        regex_all.append((i.replace(" ", ""),  i))

    for key, values in expressions_dict.items():
        regex_all.append((values.replace(" ", ""), key))

    go(regex_all, definitions_nfas)

