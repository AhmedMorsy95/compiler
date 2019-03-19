# thompson algorithm:

# 1. for each symbol in our language construct its NFA
# 2. for each regular expression -> merge symbols NFA in appropriate way to construct its NFA
  #  ex : number NFA node(1) -(\L)> node(2) -> 10 edges with values [0-10] -> 10(\L) edges -> node(finish)
# 3. merge all theeeeeeeese together so that we have NFA for our language now

# we need to convert each regex to nfa
# to do that we need to
# take each regex and calculate its postfix taking into consideration that there might be sth like this letter(digit|letter)
# our conversion will put into list 1.instances of graph 2.operators +,*,|,$
# example a+b* becomes [a,b,*,+] where a and b are instances of class graph
# * or + are unary operations which means they must come after first operator

definitions = ["letter" , "digit" , "digits" ]


#input is 1. list of definitions as strings
#         2. list of regex as strings
def convert_regex_to_nfa(regex):

    return


def priority(c):
    if c == '(':
        return -1
    if c == '|':
        return 0
    elif c == '$' :
        return 1
    return 2 # + or *


def isOperator(c):
    operators = ['*','+','|','$']
    return operators.count(c)

def isOperatorOrBracket(c):
    operators = ['*','+','|','$','(',')']
    return operators.count(c)

def infixToPostfix(s):
    expression = []
    stack = []
    for i in s:
        if isOperator(i):
            if i == '*' or i == '+':
                expression.append(i)
            elif len(stack) == 0 :
                stack.append(i)
            else:
                while len(stack) > 0 and priority(stack[-1]) >= priority(i)  :
                    expression.append(stack.pop())
                stack.append(i)
        elif i == '(':
                stack.append(i)
        elif i == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    expression.append(stack.pop())
                stack.pop()
        else:
            expression.append(i)

    while len(stack) :
        expression.append(stack.pop())

    return expression



def addConcatenation(s):  # returns a list of items separated by expressions after adding $ as concatenation operator
    cur = []
    i = 0
    # first divide them into separated items
    while i < len(s) :
        mx = i+1
        for j in range(i+1,len(s)):
            tmp = s[i:j+1]
            if definitions.count(tmp):
                mx = j+1

        cur.append(s[i:mx])
        i = mx

    ret = [cur[0]]
    # add $ if it's required
    for i in range(1,len(cur)):
        if  isOperator(ret[-1]) and isOperator(cur[i]):
            ret.append('$')
        elif cur[i] == '(' and ret[-1] != '|':
            ret.append('$')
        elif ret[-1] == ')' and isOperator(cur[i]) == 0 :
            ret.append('$')
        elif isOperatorOrBracket(ret[-1]) == 0 and isOperatorOrBracket(cur[i]) == 0:
            ret.append('$')
        elif (ret[-1] == '*' or ret[-1] == '+') and (cur[i] != '|' and cur[i] != ')'):
            ret.append('$')

        ret.append(cur[i])

    return ret

if __name__ == '__main__':
    # testing
    print(addConcatenation("a|(b*c)+"))
    print(infixToPostfix(addConcatenation("a|(b*c)+")))