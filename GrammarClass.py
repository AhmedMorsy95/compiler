
class Grammar:

    def __init__(self,production_rules):
        self.production_rules = production_rules

    #split production in white spaces
    def split_production(production_rule):
        return production_rule.split()


    def is_ll_grammar(self):
        return True
