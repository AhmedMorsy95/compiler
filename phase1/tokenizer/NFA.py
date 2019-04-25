# thompson algorithm:

# 1. for each symbol in our language construct its NFA
# 2. for each regular expression -> merge symbols NFA in appropriate way to construct its NFA
  #  ex : number NFA node(1) -(\L)> node(2) -> 10 edges with values [0-10] -> 10(\L) edges -> node(finish)
# 3. merge all theeeeeeeese together so that we have NFA for our language now

# we need to convert each regex to nfa
# to do that we need to
# take each regex and calculate its postfix taking into consideration that there might be sth like this letter(digit|letter)
# our conversion will put into list 1.instances of graph 2.operators +,*,|,$
# example a+b* becomes [a,b,*,+] where a and b are instances of class graph
# * or + are unary operations which means they must come after first operator

from .graph import Graph
from .RegexConverter import regexConverter
from .DefinitionConverter import create_def_nfa
from .DFA import DFA
from .tokenizer import *
#input is 1. list of definitions as strings
#         2. list of regex as strings
def convert_regex_to_nfa(regex , definitions):
    '''
    convert regex input string to nfa

    :param regex: regex in string format
    rest: dictionary mapping keywords to values
    :return: nfa graph object
    '''

    # add symbols in the language & \L
    # for each regex send it with its name
    x = regexConverter()
    x.definitions_nfas = definitions
    for key, value in definitions.items():
        x.addDefinition(key)
        #value.dfs()
    # TODO : ask whether \L will give an error and should be \\L
    reserved_symbols = ["+", "*", "(", ")", "L", "="]
    for i in reserved_symbols:
        x.addSymbol(i)

    all_nfas = []

    for i in regex:

        cur = i[0].replace("\\","")
        if cur != '(' and cur != ')':
            #print(i)
            all_nfas.append(x.convertRegex(i[0],i[1]))

            #print (i[0])
            #all_nfas[-1].dfs()
#    all_nfas.append(Graph())
    a = Graph('(')
    a.accept_state.names = "("
    b = Graph(')')
    b.accept_state.names = ")"
    all_nfas.append(a)
    all_nfas.append(b)
    #all_nfas[10].dfs()
    return all_nfas

def definitions_to_nfa(definitions_dict):
    '''
    TODO Louay
    a function mapping regular definitions, punctuations, keywords and anything other than regex to nfa
    :param rest:
    :return: nfa graph object
    '''
    nfa_dict = {}
    for key, val in definitions_dict.items():
        nfa_dict[key] = create_def_nfa(val, nfa_dict)

    return nfa_dict

def combine_nfas(nfa_list):
    nfa_clone=[Graph.gClone(g) for g in nfa_list]

    #nfa_clone=nfa_list
    combined = Graph.mergeOr(nfa_clone)
    #combined.dfs()
    return combined



if __name__ == '__main__':
    # testing
    regex = [("(abc)*","alpha"),("123","numerical"),]
    nfas = convert_regex_to_nfa(regex,{})
    combined = combine_nfas(nfas)
    combined.dfs()
    dfa = DFA.nfa_to_dfa(combined)
    dfa.dfs_state()
    tokenizer.tokenize(dfa,"abcabca123")
