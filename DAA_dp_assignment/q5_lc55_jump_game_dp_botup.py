

# Problem --> dp[maxReach] == can "maxReach"th index be reached? 
# Problem to subproblems --> if 'i' can be reached (dp[i] ==True ) and if we can jump from 'i' to 'maxReach', then 'maxReach' can be reached (dp[maxReach] =True). 
# Subproblems --> Thus, dp[i] is subproblem, where i<maxReach.

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


##### Testcases ######
print( canJump([2,3,1,1,4]))