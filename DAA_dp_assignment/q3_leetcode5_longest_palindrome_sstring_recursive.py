

"""
STRATEGY::::

############ FOR SUBSEQUENCE ##########################

L(i,j) = length of the largest palindromic subsequence from index i to j

largest palindromic subsequence = LPS

BABCBAB
0123456

L(0,6) represents the length of LPS of the whole string

if str(0) == str(6):
     L(0,6) = L(1,5) + 2 ?
else:
    L(0,6) = max( L(0,5) , L(1,6) )

                      L(0,6)
            L(0,5)             L(1,6)
        L(0,4)  L(1,5)    L(1,5)    L(2,6)  
        

############ FOR SUBSTRING ##########################         
           
L(i,j) = length of the largest palindromic substring from index i to j
largest palindromic substring = LPS


L(0,6) represents the length of LPS of the whole string

if str(0) == str(6):
     L(0,6) =  L(1,5) + 2 if L(1,5) == 5
else:
    L(0,6) = max( L(0,5) , L(1,6) )

                      L(0,6)
            L(0,5)             L(1,6)
        L(0,4)  L(1,5)    L(1,5)    L(2,6)    

"""

# def LPS1(s):

#     def L(i,j):

#         if j<i or j<0 or i<0 or i>=len(s) or j>=len(s):
#             return 0

#         if i==j:
#             return 1

#         if s[i] == s[j] and (L(i+1,j-1) == j-i-1):
#             lps =  L(i+1,j-1) + 2 
#         else:
#             lps = max( L(i,j-1) , L(i+1,j) )
    
#         return lps

#     return L(0,len(s)-1)

# ###### Testcases ######
# print(LPS1("BABCBAB")) #output=7
# print(LPS1("cbbd")) #output=2
# print(LPS1("aacabdkacaa")) #output= 3


def LPS(s):

    def L(i,j):
        if j<i or j<0 or i<0 or i>=len(s) or j>=len(s):
            # print(f"i={i},j={j}, substring={s[i:j+1]} case1")
            return ""
            

        if i==j:
            # print(f"i={i},j={j}, substring={s[i:j+1]} case2")
            return s[i]
        
       
        if s[i] == s[j]:
            s3 = L(i+1,j-1)
            # print(f"i={i},j={j}, substring={s[i:j+1]} case3")
            if len(s3) == j-i-1:
                lps = s[i] + s3 + s[j]
        else:
            s1 = L(i,j-1)
            s2 = L(i+1,j)
            lps = s1 if len(s1)>=len(s2) else s2  
        
            
        print(f"substring={s[i:j+1]},i={i},j={j},lps={lps} ")
        return lps


    return L(0,len(s)-1)

##### Testcases ######
# print(LPS("BABCBAB")) #output= BABCBAB
# print(LPS("cbbd")) #output= bb
print(LPS("aacabdkacaa")) #output= 3
# print(LPS("babad"))


