import queue
from dfaState import state
from string import ascii_letters
class DFA:
    def __init__(self):
        self.accept_states = []
        self.start_state = None
        self.symbols = []

def build_transition_table():
    symbols_list = []
    for char in ascii_letters:
        symbols_list.append(char)
    for i in range(0, 9):
        symbols_list.append(str(i))

    language_symbols = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ';', '<', '=',
                        '>', '?', '{', '|', '}']
    for i in language_symbols:
        symbols_list.append(i)

    dict = {}

    for i in state.state_instances:
        dict[i.id] = []
        for j in symbols_list:
            dict[i.id].append((j,i.get_transition_state(j).id))

    return dict

def print_transition_table(d):

    symbols_list = []
    for char in ascii_letters:
        symbols_list.append(char)
    for i in range(0, 9):
        symbols_list.append(str(i))

    language_symbols = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ';', '<', '=',
                        '>', '?', '{', '|', '}']
    for i in language_symbols:
        symbols_list.append(i)
    f = open("transition.txt", "w+")

    s = "node   "
    for j in symbols_list:
        s += j
        s += "     "

    f.write(s)
    f.write("\n")

    keys = list(d.keys())

    for i in range(0, state.id):
        s = str(i) + "      "
        lst = d.get(keys[i])
        for j in lst:
            s += str(j[1])
            n = 6 - len(str(j[1]))
            s += n * " "
        f.write(s)
        f.write("\n")

    f.close()
def nfa_to_dfa(nfa):
    symbols_list = []
    for char in ascii_letters:
        symbols_list.append(char)
    for i in range(0,9):
        symbols_list.append(str(i))

    language_symbols = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',';', '<', '=', '>', '?', '{', '|', '}']
    for i in language_symbols:
        symbols_list.append(i)

    start_node = nfa.start_node
    start_state = state.getState(start_node.transition_nodes('@'))
    transition_table ={}
    queue_state = queue.Queue()
    queue_state.put(start_state)
    visited = [start_state]
    while(not queue_state.empty()):
        state_pop = queue_state.get()
        for symbol in symbols_list:
           s= state_pop.get_transition_state(symbol)
           if not visited.count(s):
              queue_state.put(s)
              visited.append(s)
           state_pop.add_destination(symbol,s)

    return start_state
