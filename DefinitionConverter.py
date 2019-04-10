from string import ascii_lowercase, ascii_uppercase, digits
from graph import Graph
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
                for i in range(x,y):
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

def create_def_nfa(s):
    s = replace_range_with_or(s) #replaces all ranges with |. Example: a-z -> a|b|c|d|....|z. Also removed spaces
    # infix calculation of nfa
    # At this point, the possible operators are + * | ( )
    # | is the only operation that is done on 2 NFAs
    nfa_stack = []
    operators_stack = []
    for c in s:
        if c.isalnum():
            nfa_stack.append(Graph(c))
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

    nfas_to_merge = []
    while len(nfa_stack) != 0:
        nfas_to_merge.append(nfa_stack.pop())
    nfa_stack.append(Graph.mergeOr(nfas_to_merge))
    return nfa_stack.pop()

# for testing
if __name__ == '__main__':
    regex = "a - z | A - G"
    print(replace_range_with_or(regex))
    nfa = create_def_nfa(regex)
    print(nfa)
    nfa.dfs()
