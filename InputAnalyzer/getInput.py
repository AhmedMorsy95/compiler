import re
from .definition import Definition
# Lexical Rules Input File Format
# • Lexical rules input file is a text file.
# • Regular definitions are lines in the form LHS = RHS
# • Regular expressions are lines in the form LHS: RHS
# • Keywords are enclosed by { } in separate lines.
# • Punctuations are enclosed by [ ] in separate lines
# • \L represents Lambda symbol.
# • The following symbols are used in regular definitions and regular expressions with the
# meaning discussed in class: - | + * ( )
# • Any reserved symbol needed to be used within the language, is preceded by an
# escape backslash character.


# Input file example for the above lexical rules:
# letter = a-z | A-Z
# digit = 0 - 9
# id: letter (letter|digit)*
# digits = digit+
# {boolean int float}
# num: digit+ | digit+ . digits ( \L | E digits)
# relop: \=\= | !\= | > | >\= | < | <\=
# assign: =
# { if else while }
# [; , \( \) { }]
# addop: \+ | -
# mulop: \* | /


# from this file we need
# 1. save regex and definitions
# 2. extract keywords , reserved symbols , punctuation sybmols
# 3. given a character/string return if it satisfies a definition or not


def read_input(file_path):
    '''
    Function reads input text file containing lexical rules,
    1- interprets regular definitions, maps each def to its interpretation
    2- maps regular expression names to their strings to be interpreted later in another function
    3- keywords and punctuations are collected from the file
    4- reserved symbols and any other necessary stuff are mapped


    :param file_path: the path to the text file

    :return: dictionary
    '''
    with open(file_path, 'r') as file:
        file_lines = file.readlines()
        file.close()
    keywords_list = []
    punc_list = []
    definitions_list = []
    keywords_regex = re.compile(r"\{.*\}")
    punc_regex = re.compile(r"\[.*\]")
    definitions_regex = re.compile(r"([a-z]|[A-Z])*[ \t]*=.+")
    for line in file_lines:
        if keywords_regex.match(line) is not None:
            keywords_list.extend([ k for k in line[1:-2].split(' ') if k != ''])
        elif punc_regex.match(line) is not None:
            elements = line[1:-2].split(' ')
            for element in elements:
                if re.match(r"\\.", element) is not None:
                    punc_list.append(element[1:])
                else:
                    punc_list.append(element)
        elif definitions_regex.match(line) is not None:
            definitions_list.append(Definition(line))
    return {
    "keywords": keywords_list,
    "punctuation": punc_list,
    "definitions": definitions_list,
    "expressions": []
    }

# now we have the regex
