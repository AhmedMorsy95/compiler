from .dfaState import state
from .getInput import read_input
from .NFA import definitions_to_nfa
from .dfaState import state
from .min_state import min_state
from .RegexConverter import regexConverter
from .node import Node
from .graph import Graph
import tokenizer.NFA as NFA
import tokenizer.DFA as DFA
import tokenizer.minimization as minimization
from string import ascii_letters
from .NodeGenerator import  NodeGenerator

class Token:
    def __init__(self, lexeme, label):
        self.lexeme = lexeme
        self.label = label

    def __str__(self):
        return self.lexeme + " -> " + self.label

def tokenize(dfa,input = "",priority = {}):
    # input is a string
    tokens = []
    i = 0
    while i < len(input):
        stack = [dfa]
        for j in range(i, len(input)):
            cur_state = stack[-1]
            next_state = cur_state.get_transition_state(input[j])
            if next_state.is_dead():
                break

            stack.append(next_state)


        while len(stack) > 0:
            cur_state = stack.pop()
            if cur_state.isAccept() and len(stack) > 0:
                labels = cur_state.getLabels()
                for k in range(0,len(labels)):
                    if priority[labels[k]] < priority[labels[0]]:
                        labels[0] = labels[k]
                tokens.append(Token(input[i:i+len(stack)], labels[0]))

                i += len(stack)
                break

        if len(stack) == 0:
            # print("error, skipping a character")
            i+=1
    return tokens

def get_tokens(grammar_file_name, input_file_name, print_tokens=False, minimize=False):

    keywords_list, punc_list, definitions_dict, expressions_dict = read_input(grammar_file_name)
    # keywods_list is a list of strings containg the keywords
    # punc_list is a list of strings containg the punctuation symbols
    # definitions_dict is a dictionary, the key (string) is the definition name, and the value is the regex string that represents the definition
    # expressions_dict is a dictionary, the key (string) is the expression name, and the value is the regex string that represents the expression

    definitions_nfas = definitions_to_nfa(definitions_dict)
    # definitions_nfas is a dictionary, the key (string) is the definition name, and the value is the corresponding NFA of that definition (Graph object)

    regex = []
    for i in keywords_list:
        regex.append((i.replace(" ", ""), i))

    for i in punc_list:
        regex.append((i.replace(" ", ""),  i))

    for key, values in expressions_dict.items():
        regex.append((values.replace(" ", ""), key))

    # regex = [("(abc)*", "alpha"), ("123", "numerical")]
    #1. convert regex into nfa
    priority = {}
    sum = 0
    for i in regex:
        priority[i[1]] = sum
        sum += 1

    nfas = NFA.convert_regex_to_nfa(regex, definitions_nfas)
    #2. combine nfas together
    combined = NFA.combine_nfas(nfas)

    #3. convert nfa to dfa
    dfa = DFA.nfa_to_dfa(combined)
    if print_tokens:
        print(len(state.state_instances))

    #4. minimize dfa
    if minimize:
        minimization.minimization_states()

    if print_tokens:
        print(len(min_state.class_instance))

    #5. tokenization
    with open(input_file_name, 'r') as file:
        file_lines = file.readlines()
        file.close()

    i = 0
    all_tokens = []
    for line in file_lines:
        line_tokens = tokenize(dfa,line,priority)
        all_tokens.extend(line_tokens)
        if print_tokens:
            print("Line " + str(i + 1) + ':')
            for token in line_tokens:
                print(token)
            print('\n')
        i += 1

    return all_tokens
