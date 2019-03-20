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


from RegexConverter import regexConverter
#input is 1. list of definitions as strings
#         2. list of regex as strings
def convert_regex_to_nfa(regex , rest):
    '''
    convert regex input string to nfa

    :param regex: regex in string format
    rest: dictionary mapping keywords to values
    :return: nfa graph object
    '''
    x = RegexConverter()
    reservedSymbols = ["+", "-", "*", "/", "=", ",", "{", "}", "(", ")", ",", ";", "\\"]
    for i in reservedSymbols:
        x.addSymbol(i)

    return None

def definitions_to_nfa(rest):
    '''
    TODO Louay
    a function mapping regular definitions, punctuations, keywords and anything other than regex to nfa
    :param rest:
    :return: nfa graph object
    '''
    return

def combine_nfas(nfa_list):
    combined = None
    return combined



if __name__ == '__main__':
    # testing
    # print(addConcatenation("a|(b*c)+"))
    # print(infixToPostfix(addConcatenation("a|(b*c)+")))
