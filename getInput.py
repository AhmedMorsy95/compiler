
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

    :return: dictionary with

    keys :{ reg_def_name1 : (for example: letter) , reg_def_name2, regex_name1, regex_name2, keywords, punctuations,
     reserved_symbols, ..etc}

    and values : { [a,b,c,d,e....z], [reg_def_values2], "rejex_string1", "rejex_string2", [for, while, if ..etc],
      punctuations_values, ...etc }

    '''


# now we have the regex