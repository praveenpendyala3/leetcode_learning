
# Given num and exp, find num^exp using recursion

def power(num,exp):
    if exp == 0:
        return 1
    
    return num*power(num,exp-1)

print(power(2,52))

