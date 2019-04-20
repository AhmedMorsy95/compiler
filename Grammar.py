
class Grammar:

    # production rules which is a dictionary
    # start symbol is a string
    def __init__(self,production_rules,start_symbol):
        self.production_rules = production_rules
        self.start_symbol = start_symbol

    def is_ll_grammar(self):
        return True

    def get_start_symbol(self):
        return self.start_symbol

    def get_children(self,non_terminal):
        return self.production_rules[non_terminal]

    def is_terminal(self,string):
        keys = production_rules.keys()
        if string in keys:
            return False
        return True

    def get_non_terminals(self):
        return self.production_rules.keys()