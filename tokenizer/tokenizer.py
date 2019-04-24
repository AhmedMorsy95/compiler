from .dfaState import state

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
