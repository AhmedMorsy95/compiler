# a state is the building block for dfa
from NodeGenerator import NodeGenerator
class state:

    state_Nodes = [] # keep all combinations of nodes i met so far
    state_instances = [] # keep instances i made so far corresponding to combination of nodes in state nodes
    id = 0 # id is also position in state instances

    def sortHelper(node):
        return node.id

    @staticmethod
    def getState(nodes): # if this state already exists return it
        nodes = sorted(nodes,key=state.sortHelper)

        if state.state_Nodes.count(nodes):
            return state.state_instances[state.state_Nodes.index(nodes)]

        return state(nodes)

    def __init__(self,nodes):
        # sort nodes according to ids
        nodes = sorted(nodes,key=state.sortHelper)
        state.state_Nodes.append(nodes)
        state.state_instances.append(self)
        self.destinations = {} # we add in it a pair (char,state number)
        self.id = state.id
        state.id += 1

    @staticmethod
    def getNodeFromID(id):
        return state.state_instances[id]

    def getStateNodes(self):
        return state.state_Nodes[self.id]

    def addDestination(self,char,state_to):
            # only 1 state_to for each char, so we dont need a list
            self.destinations[char] = state_to


if __name__ == '__main__':
    x = NodeGenerator.getInstance()
    a = x.make_node()
    b = x.make_node()
    c = x.make_node()

    y = state.getState([a,b])
    z = state.getState([a,b])
    print(y,z)