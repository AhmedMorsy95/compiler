# a state is the building block for dfa
from .NodeGenerator import NodeGenerator
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
        self.destinations = {} # we add in it a pair (char,state)
        self.id = state.id
        self.labels = {}
        self.accept_state = False
        state.id += 1


    @staticmethod
    def getNodeFromID(id):
        return state.state_instances[id]

    def get_state_nodes(self):
        return state.state_Nodes[self.id]

    def add_destination(self,char,state_to):
            # only 1 state_to for each char, so we dont need a list
            self.destinations[char] = state_to

    def get_transition_state(self,char):
        nodes = self.get_state_nodes()
        all_nodes = set()
        for i in nodes:
            child_nodes = i.transition_nodes(char)
            for j in child_nodes:
                all_nodes.add(j)

        my_nodes = []
        for i in all_nodes:
            my_nodes.append(i)

        return state.getState(my_nodes)

    def is_dead(self):
        nodes = self.get_state_nodes()
        if len(nodes) == 0:
            return True
        return False

    def isAccept(self):
        nodes = self.get_state_nodes()

        for i in nodes:
            if i.isFinish:
                return True

        return False

    def getLabels(self):
        lbls = []
        nodes = self.get_state_nodes()
        for i in nodes:
            if i.names != "" and lbls.count(i.names) == False:
                lbls.append(i.names)

        return lbls
    def dfs_test(self,cur,visited,path):
        if visited.count(cur):
            return
        if cur.isAccept():
            print(path , cur.getLabels())

        visited.append(cur)
        for key, value in cur.destinations.items():
            path.append(key)
            self.dfs_test(value,visited,path)
            path.pop()
        visited.pop()

    def dfs_state(self):
        visited = []
        path = []
        self.dfs_test(self,visited,path)
