

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

def LPS(s):

    l = len(s)
    dp = [["" for _ in range(l)] for _ in range(s)]

    def L(i,j):

        if j<i or j<0 or i<0 or i>=len(s) or j>=len(s):
            return ""

        if i==j:
            dp[i][j] = s[i]
            # return s[i]
       
        if dp[i][j] != "":
            return dp[i]

        if s[i] == s[j]:
            s3 = L(i+1,j-1)
            if len(s3) == j-i-1:
                lps = s[i] + s3 + s[j]
        else:
            s1 = L(i,j-1)
            s2 = L(i+1,j)
            lps = s1 if len(s1)>len(s2) else s2  
    
        return lps

    return L(0,len(s)-1)

###### Testcases ######
print(LPS("BABCBAB")) #output= BABCBAB
print(LPS("cbbd")) #output= bb
