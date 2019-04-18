class NonTerminal:
#this class to carry Non terminal name and its children (its production )

    def __init__(self, non_terminal_name, children):
        self.name = non_terminal_name
        #list of Non terminal and terminals
        self.children = children


    def add_child(self,child):
        self.children.append(child);


    def get_children(self):
        return self.children;


