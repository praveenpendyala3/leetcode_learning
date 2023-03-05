
def canPartition(nums):
    
    sumval = sum(nums)

    # If sum is odd, return false. Cannot divide by 2.
    if sumval%2 !=0:
        return False

    dp = {}

    # CheckSum(sum,i) = Check if the sum accumulated upto index (i-1) equals totalsum/2 of the full list
    def checkSum(sum,i):
        if sum == sumval//2:
            dp[(sum,i)] = True
            # return dp[(sum,i)]
        
        if i == len(nums): # Index out of bounds.
            dp[(sum,i)] = False
            # return  dp[(sum,i)]

        if (sum,i) in dp:
            return dp[(sum,i)]

        #take
        take = checkSum(sum+nums[i],i+1)
        dp[(sum+nums[i],i+1)] = take
        #not take
        nottake = checkSum(sum, i+1)
        dp[(sum,i+1)] = nottake

        dp[(sum,i)] = take or nottake
        
        return dp[(sum,i)]
    
    return checkSum(0,0)

##### Testcases ######
print(canPartition([1,5,11,5])) # Ans = True
print(canPartition([1,2,3,5])) # Ans = False

