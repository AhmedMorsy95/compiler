from NodeGenerator import NodeGenerator
from node import *
import queue

# this class represents a single nfa that has a start node and maybe 0 or more accept (finish) nodes

class Graph:

    def __init__(self , char, node_generator, start = None, finish = None):
        # constructor makes a simple start node and accept state connected by an edge
        if(start == None):
            self.start_node = node_generator.make_node(isStart = True)
            self.accept_state = node_generator.make_node(isFinish = True)
            self.start_node.add_destination_node(char, self.accept_state)
            self.all_accept_states=[]

        else: # make custom non-simple graphs (like ones after operations)
            self.start_node = start
            self.accept_state = finish
            self.start_node.add_destination_node(char, self.accept_state)
            self.all_accept_states = []

    def get_start(self):
        return self.start_node

    def get_all_accept(self):
        return self.all_accept_states

    def get_accept(self):
        return self.accept_state

    def bfs(self): # returns list of finishes (accept states)
        q = queue.Queue()
        q.put(self.start)
        finishes = []
        print("bfs starts\n")
        while not q.empty():
            top = q.get()
            if top.isFinish:
                finishes.append(top)
            for i in top.edges:
                q.put(i[0])
                print(i[1])
        return finishes

    def go(self,cur,s):
        if cur.isFinish:
            print(s)
            return
        for i in cur.edges:
            self.go(i[0],s+i[1])

    def dfs(self): # displaying all patterns in nfa
        print("dfs starts\n")
        self.go(self.start,"")

    @staticmethod
    def mergeOr(graphs):

        return None

    @staticmethod
    def mergeConcatenate(graphs):

        return None

    @staticmethod
    def keenClosure(graphs):

        return None

    @staticmethod
    def keenClosurePlus(graphs):

        return None
#
# if __name__ == '__main__':
#     # just messin around
#     a = Node(1)
#     c = Node(1)
#     b = Node(1)
#     d = Node(1)
#     a.add_edge(c,"hamada")
#     a.add_edge(d,"adel")
#     c.add_edge(b,"rewesh")
#     d.add_edge(b,"not rewesh")
#     g = Graph(a,[b])
#     g.bfs()
#     g.dfs()
#
