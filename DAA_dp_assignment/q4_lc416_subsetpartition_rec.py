
def canPartition(nums):
    
    sumval = sum(nums)

    # If sum is odd, return false. Cannot divide by 2.
    if sumval%2 !=0:
        return False

    # CheckSum(sum,i) = Check if the sum accumulated upto index (i-1) equals totalsum/2 of the full list
    def checkSum(sum,i):
        if sum == sumval//2:
            return True
        
        if i == len(nums): # Index out of bounds.
            return False

        #take
        take = checkSum(sum+nums[i],i+1)
        #not take
        nottake = checkSum(sum, i+1)

        return take or nottake
    
    return checkSum(0,0)

##### Testcases ######
print(canPartition([1,5,11,5])) # Ans = True
print(canPartition([1,2,3,5])) # Ans = False

