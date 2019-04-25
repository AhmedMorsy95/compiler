from string import ascii_lowercase, ascii_uppercase, digits
from .graph import Graph
operators = ['*','+','|']

def priority(c):
    if c == '(':
        return -1
    if c == '|':
        return 0
    return 2 # + or *

def replace_range_with_or(s):
    s = s.replace(' ','')
    expression = ''
    in_range = False
    for c in s:
        if c.isalnum():
            if not in_range:
                range_start = c
                expression += c
            else:
                in_range = False
                realm = None
                if c in ascii_lowercase:
                    realm = ascii_lowercase
                elif c in ascii_uppercase:
                    realm = ascii_uppercase
                elif c in digits:
                    realm = digits
                x = realm.find(range_start)
                y = realm.find(c)
                expression += '|'
                for i in range(x + 1,y):
                    expression += (realm[i] + '|')
                expression += realm[y]
        else:
            if not in_range:
                if c == '-':
                    in_range = True
                else:
                    expression += c
            else:
                raise Exception("Illegal " + c + " in range")
    return expression

def create_def_nfa(s, existing_definitions_nfas):
    s = replace_range_with_or(s) #replaces all ranges with |. Example: a-z -> a|b|c|d|....|z. Also removed spaces
    # infix calculation of nfa
    # At this point, the possible operators are + * | ( )
    # | is the only operation that is done on 2 NFAs
    #print('string')
    #print(s)
    nfa_stack = []
    operators_stack = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isalnum():
            j = i
            while j < len(s) and s[j].isalnum():
                j += 1
            node_name = s[i:j]
            if len(node_name) == 1:
                nfa_stack.append(Graph(node_name))
            elif node_name in existing_definitions_nfas:
                nfa_stack.append(existing_definitions_nfas[node_name])
            else:
                raise Exception("Definition " + node_name + "Needs to come first in the grammar file")
            i = j
        else:
            if c == '+':
                nfa_stack.append(Graph.keenClosurePlus(nfa_stack.pop()))
            elif c == '*':
                nfa_stack.append(Graph.keenClosure(nfa_stack.pop()))
            elif c == '(' or c == '|':
                operators_stack.append(c)
            elif c == ')':
                nfas_to_merge = []
                operators_stack.append(c)
                while operators_stack.pop() != '(':
                    nfas_to_merge.append(nfa_stack.pop())
                nfa_stack.append(Graph.mergeOr(nfas_to_merge))
            i += 1

    if len(nfa_stack) == 1:
        return nfa_stack.pop()

    nfas_to_merge = []
    while len(nfa_stack) != 0:
        nfas_to_merge.append(nfa_stack.pop())

    return Graph.mergeOr(nfas_to_merge)

# for testing
if __name__ == '__main__':
    definitions_dict = {'letter': 'a-z | A-Z', 'digit': '0 - 9', 'digits': 'digit+'}
    nfa_dict = {}
    for key, val in definitions_dict.items():
        print(replace_range_with_or(val))
        nfa_dict[key] = create_def_nfa(val, nfa_dict)
        nfa_dict[key].dfs()
