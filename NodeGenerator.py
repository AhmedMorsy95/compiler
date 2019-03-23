from node import Node

"""
Only one NodeGenerator object in program , this is the factory of nodes that gives each node a distinct non-repeatable 
id
"""
class NodeGenerator:
    instance = None # class variable shared by all objects

    @staticmethod
    def getInstance():
        if NodeGenerator.instance == None:
           return NodeGenerator()
        else:
            return NodeGenerator.instance

    def __init__(self):
        if NodeGenerator.instance != None:
            raise Exception("singleton class")
        else:
            NodeGenerator.instance = self
            self.id = 0
            # keeping all nodes just in case needed to reference any
            self.all_nodes = []

    def make_node(self, isStart= False, isFinish= False, isDead= False):
        """
        the function that is used to create a new node
        also keeps track of all generated nodes in the system for refrencing if needed

        :param isStart: boolean whether this is a start node
        :param isFinish: boolean whether this is an accept state
        :param isDead: boolean whether this is a dead state

        :return: node object n

        """

        n = Node (self.id , isStart, isFinish, isDead)
        self.id +=1
        self.all_nodes.append(n)
        return n


if __name__ == '__main__':
    # just messing around
    ng = NodeGenerator.getInstance()
    n2 = NodeGenerator.getInstance()    print(n2.id)
    n3 = NodeGenerator.getInstance()
    # n1 = ng.make_node()
    # n2 = ng.make_node()
    # n3 = ng.make_node()
    # # test having multiple destinations for one key
    # n2.add_destination_node("character" , n1.id)
    # n2.add_destination_node("character", n3.id)
    #
    # print(n1.id , n2.id, n3.id)
    # print(n2.move_destinations)
    # print("all nodes", [x.id for x in ng.all_nodes] )