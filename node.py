class Node:
    def __init__(self, id, isStart= False, isFinish= False, isDead= False):
        self.edges = []
        self.isStart = isStart
        self.isFinish = isFinish
        self.isDeadState = isDead
        # characters that have a transition to another or same state
        self.move_chars = []
        # dictionary with key of next input character and value of corresponding destination(s)
        self.move_destinations = {}
        self.id = id
        self.names = set()


    def add_destination_node(self, char, destination):
        self.move_chars.append(char)
        self.edges.append((destination,char))
        if ( char in self.move_destinations.keys() ):
            value = self.move_destinations[char]
            value.append(destination)
            self.move_destinations[char]= value
        else:

            self.move_destinations[char] = [destination]

    def add_edge(self, to, val):
        self.edges.append((to, val))

    def clearEdges(self):
        self.edges = []
        self.move_destinations = {}




