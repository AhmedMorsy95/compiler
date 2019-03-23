# need to provide it with definitions
from NodeGenerator import NodeGenerator
from graph import *
class regexConverter:

    def __init__(self):
        self.definitions = []
        self.symbols = []

    def getSymbols(self):
        return self.symbols

    def addSymbol(self,c):
        self.symbols.append("\\" + c)


    def addDefinition(self,c):
        self.definitions.append(c)

    def getDefinitions(self):
        return self.definitions

    def infixToPostfix(self,s):
        expression = []
        stack = []
        for i in s:
            if self.isOperator(i):
                if i == '*' or i == '+':
                    expression.append(i)
                elif len(stack) == 0 :
                    stack.append(i)
                else:
                    while len(stack) > 0 and self.priority(stack[-1]) >= self.priority(i)  :
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



    def separateItems(self,s):
        cur = []
        i = 0
        definitions = self.getDefinitions()
        symbols = self.getSymbols()
        while i < len(s) :
            mx = i+1
            for j in range(i+1,len(s)):
                tmp = s[i:j+1]
                if definitions.count(tmp):
                    mx = j+1
                if symbols.count(tmp):
                    mx = j+1

            cur.append(s[i:mx])
            if cur[-1] == "\L":
                cur.pop()
                cur.append("@")
            i = mx
        return cur

    def addConcatenation(self,cur):

        ret = [cur[0]]
        # add $ if it's required
        for i in range(1,len(cur)):
            if  self.isOperator(ret[-1]) and self.isOperator(cur[i]):
                ret.append('$')
            elif cur[i] == '(' and ret[-1] != '|':
                ret.append('$')
            elif ret[-1] == ')' and self.isOperator(cur[i]) == 0 :
                ret.append('$')
            elif self.isOperatorOrBracket(ret[-1]) == 0 and self.isOperatorOrBracket(cur[i]) == 0:
                ret.append('$')
            elif (ret[-1] == '*' or ret[-1] == '+') and (cur[i] != '|' and cur[i] != ')'):
                ret.append('$')

            ret.append(cur[i])

        return ret


    def priority(self,c):
        if c == '(':
            return -1
        if c == '|':
            return 0
        elif c == '$' :
            return 1
        return 2 # + or *


    def isOperator(self,c):
        operators = ['*','+','|','$']
        return operators.count(c)

    def isOperatorOrBracket(self,c):
        operators = ['*','+','|','$','(',')']
        return operators.count(c)


    # any \reserved symbol is treated as a definition
    #definitions = [] # should include definitions from

    def convertRegex(self,regex,regexName):
        symbols = self.getSymbols()
        definitions = self.getDefinitions()
        # add symbols preceded with \
        for i in range(0,len(symbols)):
            tmp = "\\" + symbols[i]
            if self.definitions.count(tmp) == 0:
                definitions.append(tmp)

        expression = self.separateItems(regex)
        expression = self.addConcatenation(expression)
        expression = self.infixToPostfix(expression)
        return self.evaluatePostfix(expression)

    def makeNFA(self,c):
        g = Graph(c)
        return g


    def getNFA(self,expression):  # expression is a string

        if self.definitions.count(expression):
            return None

        if self.symbols.count(expression):
            return self.makeNFA(expression[1:]) # skip the escape character

        return self.makeNFA(expression)


    def evaluatePostfix(self,expression):
        stack = []
        print(expression)
        for i in expression:
            if self.isOperator(i):
                if i == "*" or i == "+" :
                    cur = stack.pop()

                else: # | or $
                    a = stack.pop()
                    b = stack.pop()

                    if i == '$':
                        stack.append(Graph.mergeConcatenate([b,a]))
                    else:
                        stack.append(Graph.mergeOr([a,b]))

            else:
                stack.append(self.getNFA(i))
        return stack.pop()

# for testing
if __name__ == '__main__':
    x = regexConverter()
    x.addSymbol("L")
    g = x.convertRegex("(a|b|c|\L)Y","")
    g.dfs()


