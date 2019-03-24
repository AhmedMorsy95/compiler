from getInput import read_input
from NFA import definitions_to_nfa

keywords_list, punc_list, definitions_dict, expressions_dict = read_input("grammar.txt")
# keywods_list is a list of strings containg the keywords
# punc_list is a list of strings containg the punctuation symbols
# definitions_dict is a dictionary, the key (string) is the definition name, and the value is the regex string that represents the definition
# expressions_dict is a dictionary, the key (string) is the expression name, and the value is the regex string that represents the expression

definitions_nfas = definitions_to_nfa(definitions_dict)
# definitions_nfas is a dictionary, the key (string) is the definition name, and the value is the corresponding NFA of that definition (Graph object)
