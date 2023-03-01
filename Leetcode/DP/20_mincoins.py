def change(n,coins,dp):
    
    if n in coins:
        return 1
    
    if dp[n] != -1:
        return dp[n]

    comb = []
    for c in coins:
        if n-c>0:
            comb.append(1+change(n-c,coins,dp))
    # print(f"comb = {comb}, n = {n}")
    dp[n] = min(comb)
    return dp[n]

dp = [-1]*12
print(change(11, [1,2,5],dp))


    

