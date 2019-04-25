class Grammar:

    # production rules which is a dictionary
    # start symbol is a string
    def __init__(self,production_rules,start_symbol):
        self.production_rules = production_rules
        self.start_symbol = start_symbol
        self.epsilon = "\L"
        # print(self.is_ll_grammar())
        self.convert_to_ll_grammar()

    def convert_to_ll_grammar(self):
        if not self.is_ll_grammar():
            print("Converting grammar to LL(1)")
            ll_rules = {}
            for non_terminal, rules in self.production_rules.items():
                if self.is_immediate_left_recursive(non_terminal, rules):
                    left_recursive = []
                    non_left_recursive = []
                    for rule in rules:
                        if rule[0] == non_terminal:
                            left_recursive.append(rule)
                        else:
                            non_left_recursive.append(rule)
                    non_terminal_dash = non_terminal + "`"
                    ll_rules[non_terminal] = []
                    ll_rules[non_terminal_dash] = []
                    for rule in non_left_recursive:
                        ll_rules[non_terminal].append(rule + [non_terminal_dash])
                    for rule in left_recursive:
                        ll_rules[non_terminal_dash].append(rule[1:] + [non_terminal_dash])
                    ll_rules[non_terminal_dash].append(['\L'])
                else:
                    ll_rules[non_terminal] = rules
            self.production_rules = ll_rules

    def is_immediate_left_recursive(self, non_terminal, rules):
        for rule in rules:
            if rule[0] == non_terminal:
                return True
        return False

    def is_ll_grammar(self):
        flag = True
        for non_terminal, rules in self.production_rules.items():
            flag = flag and not self.is_immediate_left_recursive(non_terminal, rules)
        return flag

    def get_start_symbol(self):
        return self.start_symbol

    def get_children(self,non_terminal):
        return self.production_rules[non_terminal]

    def get_non_terminals(self):
        return self.production_rules.keys()

    def get_terminals(self):

        terminals = set()
        non_terminals = self.get_non_terminals()
        for i in non_terminals:
            children = self.get_children(i)
            for list in children:
                for string in list:
                    if self.is_terminal(string):
                        terminals.add(string)

        return terminals

    def is_terminal(self,string):
        keys = self.production_rules.keys()
        if string in keys:
            return False
        return True
