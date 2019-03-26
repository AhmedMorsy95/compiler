from getInput import read_input
from NFA import definitions_to_nfa
from main import go
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
print([graph.dfs() for graph in def_nfas.values()])

print(def_nfas.keys())
print(def_nfas["digit"])
#print([move.move_chars for move in def_nfas.values().start_node.move_destinations.values()])

#print([graph.start_node.edges for graph in def_nfas.values()])
print("\n\ncombined regex\n\n")
regex_all = []
for i in keywords_list:
    regex_all.append((i.replace(" ", ""), i))

for i in punc_list:
    regex_all.append((i.replace(" ", ""),  i))

for key, values in expressions_dict.items():
    regex_all.append((values.replace(" ", ""), key))
print(regex_all)

print("\n\nregex to NFA\n\n")
regex=regex_all
definitions=def_nfas
nfas = NFA.convert_regex_to_nfa(regex, definitions)
print(len(nfas))
#print([g.dfs() for g in nfas])
print(nfas[0].dfs())
print(nfas[1].dfs())
print("digits+")
print(nfas[11])
print(nfas[11].dfs())

import copy
x=Graph("a")
y=copy.deepcopy(x)

print(x.dfs(),y.dfs())