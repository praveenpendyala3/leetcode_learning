

#jmpto(i) = Is it possible to jump to position i in any way?

# we look at all indexes that we can possibly jump from and recrsively check if that index can be jumped to from a previous index 

def canJump(nums):
    dp = [False for _ in range(len(nums))]
    dp[0] = True

    i=0
    for maxReach in range(1,len(nums)):
        while i < maxReach:
            if dp[i] == True and nums[i] + i >= maxReach:
                dp[maxReach] = True
                break
            i+=1
    
    return dp[-1]



print( canJump([2,3,1,1,4]))