
def fib(num,dp,rd):
    print(f'RD = {rd}, DP = {dp}')
    if num<=1:
        dp[num] = num
        return num

    if dp[num] != -1:
        return dp[num]

    dp[num] = fib(num-1,dp,rd+1) + fib(num-2,dp,rd+1)
    return dp[num]


nums = 4
dp = [-1]*(nums+1)
print(fib(nums,dp,1))
print(dp)
