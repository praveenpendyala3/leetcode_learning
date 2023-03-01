def MergeSort(A): 
    size = 1
    while size<len(A):
        start = 0 
        end = start+2*size
        while start < len(A):
            if end < len(A):
                A[start:end] = Merge(A[start:start+size],A[start+size:end])
            elif len(A[start:])>1 and len(A[start+size:])>=1:
                A[start:] = Merge(A[start:start+size],A[start+size:])
            start,end = end,end+2*size
        size = size*2

def Merge(A,B):
    i=0
    j=0
    result=[]
    while i<len(A) and j<len(B):
        if A[i]<=B[j]:
            result.append(A[i])
            i+=1
        else:
            result.append(B[j])
            j+=1

    while i<len(A):
        result.append(A[i])
        i+=1
    while j < len(B):
        result.append(B[j])
        j += 1
    return result


A = []
MergeSort(A)
print(A)
