
class Grammar:

    # production rules which is a dictionary
    # start symbol is a string
    def __init__(self,production_rules,start_symbol):
        self.production_rules = production_rules
        self.start_symbol = start_symbol
        self.epsilon = "\L"

    def is_ll_grammar(self):
        # calculated using first , follow and table
        return True

    def get_start_symbol(self):
        return self.start_symbol

    def get_children(self,non_terminal):
        return self.production_rules[non_terminal]

    def get_non_terminals(self):
        return self.production_rules.keys()

    def is_terminal(self,string):
        keys = self.production_rules.keys()
        if string in keys:
            return False
        return True
