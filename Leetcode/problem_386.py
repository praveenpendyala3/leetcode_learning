
# Given number n, print in lexicographic order. 
n = 2543

arr = []
for num in range(1,n+1):
    position =  0
    size = len(str(num))
    for i in range(size):
        position = position + int(str(num)[:i+1]) - 10**(i) + 1
        print(position)
    arr.insert(position-1, num)

print(arr)