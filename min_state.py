from dfaState import state

class min_state:
    id = 0
    class_instance = []
    map_state_to_class = {} #{state,id}

    def __init__(self, states):
        self.nodes_of_this_class = states.copy()
        self.id = min_state.id
        min_state.id +=1
        min_state.class_instance.append(self)
        self.destinations = {}
        self.accept_state = False

    def get_transition_mp(self,inputs):
        symbol_list = []
        ret_list = []
        for j in inputs:
            for i in self.nodes_of_this_class:
                states=i.get_transition_state(j)
                for k in states:
                    symbol_list.append(min_state.map_state_to_class[k])
            ret_list.append(symbol_list)

    def map_state_to_id(self):
        for i in self.nodes_of_this_class:
            min_state.map_state_to_class[i]=self.id

    def is_same(state1,state2,symbols):
        for s in symbols:
           if min_state.map_state_to_class[state1.get_transition_state] == min_state.map_state_to_class[state2.get_transition_state]:
               continue
           else:
               return False
        return True





