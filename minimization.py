from dfaState import  state
from min_state import  min_state
import queue
def minimization_states():
    initial_unaccepted_state=[]
    initial_accepted_state=[]
    number_of_states = len(state.state_Nodes)
    for s in state.state_Nodes:
        if s.isAccept():
            initial_accepted_state.append(s)
        else:
            initial_unaccepted_state.append(s)
    q = queue.Queue()
    class1 = min_state.getState(initial_unaccepted_state)
    class2 = min_state.getState(initial_accepted_state)
    q.put(class1)
    q.put(class2)
    cnt = 0
    while(not q.empty()):
        c = q.get()

