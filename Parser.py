
class Parser:

    # grammar is an instance from class grammar
    def __init__(self,grammar):
        self.grammar = grammar
        # will be filled by functions
        self.first = {}
        self.follow = {}
        self.table = None


    def initialize_dic(self,all_non_terminals):
        for non_terminal in all_non_terminals:
            self.first[non_terminal]= set ()


    def build_first(self):
        all_non_terminals = self.grammar.get_non_terminals()
        visited=[]
        self.initialize_dic(all_non_terminals)
        for non_terminal in all_non_terminals:
            if non_terminal not in visited :
                visited.append(non_terminal)
                self.dfs(non_terminal,visited)

        print(self.first)

    def build_follow(self):
      
        self.follow = dict()
        non_terminals = self.grammar.get_non_terminals()

        #initialize a set for each non terminal
        for i in non_terminals:
            dict[i] = set()

        # The first rule
        # start symbol has $ in follow

        dict[self.grammar.start_symbol].add("$")

        # The second rule
        # if A -> cBx
        # then all first of x are added to follow of B except eps


        # loop on non terminals
        for i in non_terminals:
            # get the RHS
            children = self.grammar.get_children(i)
            # loop on elements in RHS
            for list in children:
                for idx in range(0,len(list)-1):

                    # if current element is non terminal
                    if not self.grammar.is_terminal(list[idx]) :
                        # add first of the next symbol except eps
                        cur_non_terminal = list[idx]
                        following_symbol = list[idx+1]
                        first = self.first[following_symbol]

                        for k in first:
                            if k != self.grammar.epsilon:
                                dict[cur_non_terminal].add(k)

        # The third rule
        # A -> alphaB or A -> alphaBbeta and first(beta) has epsilon
        # everything in follow A is in follow B




    def build_table(self):
        return None

    def build(self):
        self.build_first()
        self.build_follow()
        self.build_table()


    def parse(self,tokens):
        return None

    def dfs(self,parent,visited):
        if self.grammar.is_terminal(parent) or parent == self.grammar.epsilon:
            self.first[parent]=set()
            self.first[parent].add(parent)
            return None
        lst = self.grammar.get_children(parent)
        children=[]
        for x in lst:
            children.append(x[0])
        for child in children:
          if child not in visited:
            visited.append(child)
            self.dfs(child,visited)
          first_of_child = self.first[child]
          for f in first_of_child:
                self.first[parent].add(f)

        return None

