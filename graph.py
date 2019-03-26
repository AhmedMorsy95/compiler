from NodeGenerator import NodeGenerator
from node import *
import queue

# this class represents a single NFA that has a start node and maybe 0 or more accept (finish) nodes

class Graph:

    def __init__(self , char, start = None, finish = None):
        # constructor makes a simple start node and accept state connected by an edge
        node_generator = NodeGenerator.getInstance()
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

    # needs modification
    def bfs(self): # returns list of finishes (accept states)
        q = queue.Queue()
        q.put(self.start_node)
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

    def go(self,cur,s,visited = []):

       # print(s,cur.names,cur.id)
        if visited.count(cur.id):
            return

        if cur.isFinish:
            print(s , cur.names,cur.id)
            return

        visited.append(cur.id)


        for i in cur.edges:
            z = s
            z.append([i[1],[i for i in i[0].names],cur.id])
            self.go(i[0],z)
            z.pop()

        visited.pop()

    def dfs(self): # displaying all patterns in nfa
        print("dfs starts\n")
        self.go(self.start_node,[])

    @staticmethod
    def mergeOr(graphs):
        g = Graph("@")
        g.start_node.clearEdges()
        for i in graphs:
            g.start_node.add_destination_node("@",i.start_node)
            i.start_node.isStart = 0
            i.accept_state.add_destination_node("@",g.accept_state)
            i.accept_state.isFinish = 0
            for j in i.start_node.names:
                g.start_node.names.add(j)
                g.accept_state.names.add(j)
        return g

    @staticmethod
    def mergeConcatenate(graphs):
        a = graphs[0]
        b = graphs[1]
        a.accept_state.add_destination_node("@",b.start_node)
        a.accept_state.isFinish = 0
        a.accept_state = b.accept_state
        return a

    @staticmethod
    def keenClosure(graph):
        """
        uses the kleen closure operator on a graph to produce a new graph using thompson algorithm
        :param graph: a graph
        :return:
        """
        n = NodeGenerator.getInstance()
        g = Graph("@")
        # g.start_node.clearEdges()
        # repeat more than once
        graph.accept_state.add_destination_node("@", graph.start_node)
        # add new finish with edge epsilon
        graph.accept_state.add_destination_node("@", g.accept_state)
        graph.accept_state.isFinish = 0
        # add new start
        g.start_node.add_destination_node("@", graph.start_node)
        graph.start_node.isStart = 0
        # repeat zero times
        return g

    @staticmethod
    def keenClosurePlus(graphs):
       graph = []
       graph.append(graphs)
       graph.append(Graph.keenClosure(graphs))
       return Graph.mergeConcatenate(graph)
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
