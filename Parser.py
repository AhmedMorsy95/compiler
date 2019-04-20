
class Parser:

    # grammar is an instance from class grammar
    def __init__(self,grammar):
        self.grammar = grammar
        # will be filled by functions
        self.first = None
        self.follow = None
        self.table = None



    def build_first(self):
        return None

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