

nums = [0,1,0,3,12]

p1 = len(nums)
for i in range(len(nums)):
    if nums[i] == 0:
        p1 = i
        break

p2 = p1+1

while p1<len(nums) and p2<len(nums):
    if nums[p2] != 0:
        nums[p1],nums[p2] = nums[p2], nums[p1]
        p1 = p1+1
    
    p2 = p2+1

print(nums)
