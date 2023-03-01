s = '[]'


def validParan(s):
    openlist = ""
    print(s, openlist)
    for char in s:
        # When strings are opening:
        if char == "(":
            openlist = openlist + "1"
        if char == "{":
            openlist = openlist + "2"
        if char == "[":
            openlist = openlist + "3"
        
        # When strings are closing:


        if char == ")":
            if len(openlist) == 0 or openlist[-1] != "1":
                return False
            openlist = openlist[:-1]
        if char == "}":
            if len(openlist) == 0 or openlist[-1] != "2":
                return False
            openlist = openlist[:-1]
        if char == "]":
            if len(openlist) == 0 or openlist[-1] != "3":
                return False
            openlist = openlist[:-1]
        
    if len(openlist) == 0:
        return True
    else:
        return False


print(validParan("]"))

