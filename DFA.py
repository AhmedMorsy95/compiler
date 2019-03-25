import queue
from dfaState import state
class DFA:
    def __init__(self):
        self.accept_states = []
        self.start_state = None
        self.symbols = []



def nfa_to_dfa(nfa):
    symbols_list = ['a','b','c','d','e','f']
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