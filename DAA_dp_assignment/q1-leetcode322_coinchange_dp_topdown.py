def coinChange(coins, amount):

    dp = [-1 for _ in range(amount+1)]

    def change(n):
        
        if n in coins:
            dp[n] = 1

        if dp[n] != -1:
            return dp[n]

        mini = 100000 # more than maximum value that is possible base don constraints
        for c in coins:
            if c<n:
                mini = min(mini,1+change(n-c))
        
        dp[n] = mini                 
        return dp[n]

    if amount==0:
        return 0
    sol = change(amount)
    return -1 if sol==100000 else sol

     
###### Testcases ######
print(coinChange([1,2,5],11)) #output=3
print(coinChange([2],3)) #output=-1
print(coinChange([1],0)) #output=0