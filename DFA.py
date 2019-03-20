def nfa_to_dfa(nfa):
    print()
    """
        returns graph where each state has a list of pairs (state to go to in case of this symbol , symbol)
    """

    """
     subset construction algorithm :

     1. start with the start node add all nodes where edge connecting with start node is \L (eps) -> call it a state s
     2. for each symbol determine move(s,symbol) which is state after moving over edge with value = symbol and add it to queue/stack (it wasnot added before)
     3. keep doing this until queue/stack is empty
     4. we have a transition table now, any state containing at least 1 finishing state in our language is an (F) state
    """