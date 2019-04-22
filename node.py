import queue

class Node:
    transition_states = {}

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
        self.names = ""


    def add_destination_node(self, char, destination):
        self.move_chars.append(char)
        self.edges.append((destination, char))
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

    def transition_nodes(self,char):
        ret = []
        if char == '@':
            ret.append(self)

        saved_char = char
        if char not in Node.transition_states.keys():
            Node.transition_states[char] = {}
        else:
            if self in Node.transition_states[char].keys():
                return Node.transition_states[char][self]

        q = queue.Queue()
        visited = set()
        if (char in self.move_destinations.keys()):
            for i in self.move_destinations[char]:
                if not i in visited:
                    q.put(i)
                    visited.add(i)

        char = "@"
        while not q.empty():
            cur = q.get()
            ret.append(cur)
            if ( char in cur.move_destinations.keys() ):
                list = cur.move_destinations[char]
                for i in list:
                    if not i in visited:
                        visited.add(i)
                        q.put(i)

        Node.transition_states[saved_char][self] = ret
        return ret
