def coinChange(coins, amount):

    def change(n):
        
        if n in coins:
            return 1
        
        if n==0:
            return -1

        mini = 100000 # more than maximum value that is possible base don constraints
        for c in coins:
            if c<n:
                mini = min(mini,1+change(n-c))

        return mini                

    if amount==0:
        return 0
    solution = change(amount) 
    return -1 if solution==100000 else solution
    
    
    

print(coinChange([1,2,5],11)) #output=3
print(coinChange([2],3)) #output=-1
print(coinChange([1],0)) #output=0