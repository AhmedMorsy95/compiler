from node import  Node
class NodeGenerator:
    def __init__(self):
        self.id=0
        # keeping all nodes just in case needed to reference any
        self.all_nodes=[]

    def make_node(self, isStart= False, isFinish= False, isDead= False):
        n = Node (self.id , isStart, isFinish, isDead)
        self.id +=1
        self.all_nodes.append(n)
        return n

if __name__ == '__main__':
    # just messing around
    ng=NodeGenerator()
    n1 = ng.make_node()
    n2 = ng.make_node()
    n3 = ng.make_node()
    # test having multiple destinations for one key
    n2.add_destination_node("character" , n1.id)
    n2.add_destination_node("character", n3.id)

    print(n1.id , n2.id, n3.id)
    print(n2.move_destinations)
    print("all nodes", [ x.id for x in ng.all_nodes] )