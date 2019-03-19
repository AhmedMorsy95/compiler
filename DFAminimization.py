
# given a transition table , minimize the states
# algorithm:
#   1. divide states into 2 classes F(accepted state)  and S
#   2. keep dividing classes until for each class all states go to the same class after all transitions


def minimize(DFA):
    # returns graph same structure as DFA but probably with less states
    print()