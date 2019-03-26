from getInput import read_input
from NFA import definitions_to_nfa
import tokenizer
from dfaState import state
from RegexConverter import regexConverter
from node import Node
from graph import Graph
import NFA
import DFA
from NodeGenerator import  NodeGenerator

keywords_list, punc_list, definitions_dict, expressions_dict = read_input("grammar.txt")

print("keywords")
print(keywords_list)
print("punctuations")
print(punc_list)
print("definitions")
print(definitions_dict.keys())
print(definitions_dict.values())
print("expressions")
print(expressions_dict.keys())
print(expressions_dict.values())
print("definitions nfas")
def_nfas=definitions_to_nfa(definitions_dict)
print(def_nfas.keys())
print([graph.start_node.move_chars for graph in def_nfas.values()])
print([graph.start_node.edges for graph in def_nfas.values()])