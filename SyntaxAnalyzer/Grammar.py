class Grammar:

    # production rules which is a dictionary
    # start symbol is a string
    def __init__(self,production_rules,start_symbol):
        self.production_rules = production_rules
        self.start_symbol = start_symbol
        self.epsilon = "\L"
        # print(self.is_left_recursive(stack = [self.start_symbol]))
        self.convert_to_ll_grammar()

    def convert_to_ll_grammar(self):
        print(self.production_rules)
        self.eliminate_non_immediate_left_recursion()
        print(self.production_rules)
        self.eliminate_immediate_left_recursion()
        print(self.production_rules)

    def eliminate_immediate_left_recursion(self):
        if not self.is_immediate_left_recursive():
            print("Converting immediate left recursive grammar to LL(1) grammar")
            ll_rules = {}
            for non_terminal, rules in self.production_rules.items():
                if self.is_rule_immediate_left_recursive(non_terminal, rules):
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

    def is_rule_immediate_left_recursive(self, non_terminal, rules):
        for rule in rules:
            if rule[0] == non_terminal:
                return True
        return False

    def is_immediate_left_recursive(self):
        flag = True
        for non_terminal, rules in self.production_rules.items():
            flag = flag and not self.is_rule_immediate_left_recursive(non_terminal, rules)
        return flag

    def eliminate_non_immediate_left_recursion(self):
        if self.is_left_recursive(stack = [self.start_symbol]):
            print("Converting non immediate left recursive grammar to immediate left recursive grammar")
            ll_rules = {}
            for non_terminal, rules in self.production_rules.items():
                ll_rules[non_terminal] = []
                for rule in rules:
                    if rule[0] in self.get_non_terminals():
                        composite_non_terminal = rule[0]
                        for composite_rule in self.production_rules[composite_non_terminal]:
                            ll_rules[non_terminal].append(composite_rule + rule[1:])
                    else:
                        ll_rules[non_terminal].append(rule)
            self.production_rules = ll_rules


    def is_left_recursive(self, stack = [], visited = [], flag = False):
        if len(stack) > 0:
            symbol = stack.pop()
            if symbol in self.get_non_terminals():
                if symbol in visited:
                    flag = True
                else:
                    visited.append(symbol)
                    for rule in self.production_rules[symbol]:
                        stack.append(rule[0])
                    flag = flag or self.is_left_recursive(stack, visited, flag)
                    return flag
            else:
                flag = False
            return flag or self.is_left_recursive(stack, visited, flag)
        else:
            return False

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
