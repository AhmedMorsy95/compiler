def read_input(file_name):
    f = open(file_name, "r")
    contents = f.read().split('#')
    lines = dict()

    first = True
    start_symbol = ""

    for line in contents:
        if len(line) == 0:
            continue

        lhs,rhs = split_line(line)
        lines[lhs] = rhs

        if first:
            start_symbol = lhs
            first = False


    return lines,start_symbol

# splits line on ::= , to get lhs and rhs
# then splits on |
# then removes noise like extra spaces , ' and \n

def split_line(line):

    list1 = line.split("::=")
    lhs = list1[0]
    rhs = list1[1].split('|')

    modified_rhs = []

    for all in rhs:
        one_side = all.split(" ")
        one_side = list(filter(None,one_side))

        for i in range(0,len(one_side)):
            one_side[i] = one_side[i].replace(" ","")
            one_side[i] = one_side[i].rstrip()
            if one_side[i][0] == "‘"  or one_side[i][0] == "’" or one_side[i][0] == "'":
                one_side[i] = one_side[i].replace("‘","")
                one_side[i] = one_side[i].replace("’", "")
                one_side[i] = one_side[i].replace("'", "")

        modified_rhs.append(one_side)

    return lhs.replace(" ",""),modified_rhs
