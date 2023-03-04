

#jmpto(i) = Is it possible to jump to position i in any way?

# we look at all indexes that we can possibly jump from and recrsively check if that index can be jumped to from a previous index 

def canJump(nums):
    
    dp = [False for _ in range(len(nums))]
    dp[0] = True

    def jmpto(i):
               
        if dp[i]:
            return True 

        jmpPossible = False
        for k in range(i):
            if nums[k] >= i-k:
                jmpPossible = jmpPossible or jmpto(k)
        dp[i] = jmpPossible
        return dp[i]

    return jmpto(len(nums)-1)


print( canJump([2,3,1,1,4]))