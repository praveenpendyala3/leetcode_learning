

def stairs(n):
    if n<=1:
        return 1
    if dp[n] != -1:
        return dp[n] 
    
    dp[n]=stairs(n-1)+stairs(n-2)
    
    return dp[n]


n=3
dp=[-1]*(n+1)
print(stairs(n))