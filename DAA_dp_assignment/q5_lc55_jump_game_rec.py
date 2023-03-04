

#jmpto(i) = Is it possible to jump to position i in any way?

# we look at all indexes that we can possibly jump from and recrsively check if that index can be jumped to from a previous index 

def canJump(nums):
    

    def jmpto(i):

        if i==0:
            return True
        
        jmpPossible = False
        for k in range(i):
            if nums[k] >= i-k:
                jmpPossible = jmpPossible or jmpto(k)
        
        return jmpPossible

    return jmpto(len(nums)-1)


print( canJump([2,3,1,1,4]))