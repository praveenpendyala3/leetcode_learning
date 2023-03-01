# arr = [2,0,1]

# X = []
# for i in range(len(arr)):
#     for k in range(i+1):
#         if len(arr[k:i+1])>0:
#             X.append(arr[k:i+1])
        
# X1 = [val for i, val in enumerate(X) if val not in X[:i]]

# MEX_dict = {}
# for lst in X1:
#     MEX=0
#     for elem in sorted(lst):
#         if elem==MEX:
#             MEX=MEX+1

#     if MEX not in MEX_dict.keys():
#         MEX_dict[MEX] = 1
#     else:
#         MEX_dict[MEX] = MEX_dict[MEX] + 1

# final_list = []
# for key in sorted(MEX_dict.keys()):
#     final_list.append(MEX_dict[key])

# print(final_list)


regionStart = [7,3,9,5,6,7]
regionEnd = [20,4,10,5,9,11]

regions = []

for i in range(len(regionStart)):
     regions.append([regionStart[i],regionEnd[i]])

regions = sorted(regions) 

print(regions)
print(len(regions))
move = 0
for i in range(len(regions)):
    fail = 0
    for j in range(i+1,len(regions)):
        if regions[i][1] < regions[j][0]:
            fail = fail+1
        if fail == len(regions)-i-1:
            move = move + 1

print(move)



