
class Parser:

    # grammar is an instance from class grammar
    def __init__(self,grammar):
        self.grammar = grammar
        # will be filled by functions
        self.first = {}
        self.follow = {}
        self.table = None



    def build_first(self):
        all_non_terminals = self.grammar.get_non_terminals()
        visited = []
        for non_terminal in all_non_terminals:
            if non_terminal not in visited:
                visited.append(non_terminal)
                self.dfs(non_terminal,visited)

    def build_follow(self):

        return None

    def build_table(self):
        return None

    def build(self):
        self.build_first()
        self.build_follow()
        self.build_table()


    def parse(self,tokens):
        return None

    def dfs(self,parent,visited):
        if self.grammar.is_terminal(parent):
            self.first[parent]=[parent]
            return None
        lst = self.grammar.get_children(parent)
        children=[]
        children.append([x[0] for x in lst])
        for child in children:
          if child not in visited:
            visited.append(child)
            first_of_child = self.dfs(child)
            for f in first_of_child:
                self.first[parent].append(f)
          else:
            first_of_child = self.first[child]
            for f in first_of_child:
                self.first[parent].append(f)



        return None

