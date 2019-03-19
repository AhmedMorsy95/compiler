from graph import Edge

class Node:
    def __init__(self):
        self.edges = []
        self.isStart = False
        self.isFinish = False
        self.isDeadState = False
        # characters that have a transition to another or same state
        self.move_chars = []
        # dictionary with key of next input character and value of corresponding destination(s)
        self.move_destinations = {}

    def addEdge(self,to,val):
        self.edges.append((to,val))
