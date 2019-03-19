
from node import *
import queue
# helper class for NFAs


class Edge:
    def __init__(self,to,val):
        self.to = to
        self.val = val

# this class represents a single nfa
class Graph:

    def __init__(self , start , finish,name=""):
        self.start = start
        self.finish = finish
        self.name = name
        self.start.isStart = True
        for i in self.finish:
            i.isFinish = True

    def bfs(self): # returns list of finishes
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

if __name__ == '__main__':
    # just messin around
    a = Node(1)
    c = Node(1)
    b = Node(1)
    d = Node(1)
    a.add_edge(c,"hamada")
    a.add_edge(d,"adel")
    c.add_edge(b,"rewesh")
    d.add_edge(b,"not rewesh")
    g = Graph(a,[b])
    g.bfs()
    g.dfs()

