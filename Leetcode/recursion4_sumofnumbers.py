# Add first 'n' natural numbers




def addNums(n):
    if n == 1:
        return 1 

    return n + addNums(n-1)


print(addNums(5))