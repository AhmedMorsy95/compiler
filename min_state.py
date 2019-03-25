from dfaState import state

class min_state:
    #map every state to new min_state
    min_state_class ={} #{state,id}
    id=0
    new_state_nodes=[]

    def get_id(node):
        return node.id

    def __init__(self,nodes):
        # sort nodes according to ids
        nodes = sorted(nodes,key=state.sortHelper)
        min_state.new_state_nodes.append(nodes)
        self.destinations = {} # we add in it a pair (char,state)
        self.id = state.id
        self.labels = {}
        self.accept_state = False
        state.id += 1

    def add_destination(self, char, state_to):
        # only 1 state_to for each char, so we dont need a list
        self.destinations[char] = state_to

    def get_destination(self,char):
        return self.destinations[char]

    def define_class(self,s,class_belong_to):
        self.min_state_class[s]=class_belong_to


