
def SelectionSort(nums):
    #Repeatedly find min value, put at beginning

    i = 0
    j = i

    while i <len(nums):
        min = i
        while j<len(nums):
            if nums[j] < nums[min]:
                min = j
            j +=1

        nums[i],nums[min] = nums[min],nums[i]
        i = i+1  
        j = i



nums = [99,-101,2,3,8,1,0]
SelectionSort(nums)
print(nums)