from getInput import read_input
from NFA import convert_regex_to_nfa
from DFA import nfa_to_dfa
from DFAminimization import minimize
class LexicalAnalyzerGenerator:
    """
    Factory class that is instantiated to create a Lexical Analyzer object and encapsulates the whole creation process
    """

    def __init__(self):
        self.NFAs = []
        self.rules = {}
        # use the functions defined outside
        self.read_input_file = read_input()
        self.regex_to_nfa = convert_regex_to_nfa()
        self.nfa_to_dfa = nfa_to_dfa()
        self.minimize_dfa = minimize()

    def generate(self,input_file):
        regex = self.read_input_file(input_file)
        nfa = self.regex_to_nfa(regex)
        dfa = self.nfa_to_dfa(nfa)
        min_dfa = self.minimize_dfa(dfa)

        return lex_analyzer,trans_table




if __name__ == '__main__':
    # for testing only, then all those functions will be incapsulated in one
    input_file = "rules.txt"
    LAG = LexicalAnalyzerGenerator()
    regex = LAG.read_input_file(input_file)
    nfa = LAG.regex_to_nfa(regex)
    dfa = LAG.nfa_to_dfa(nfa)
    min_dfa = LAG.minimize_dfa(dfa)
    # the only line that will actually be used:
    lexical_analyzer, transition_table = LAG.generate(input_file)


