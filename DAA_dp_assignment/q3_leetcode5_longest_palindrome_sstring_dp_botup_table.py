

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
    ls = len(s)
    dp = [[False for _ in range(ls)]  for _ in range(ls)] # Empty dp 2d array

    lps = ""

    for i in range(ls):
        dp[i][i] = True
        if i+1<ls and s[i]==s[i+1]:
            dp[i][i+1] = True
            lps = s[i:i+2]
    

    for diff in range(2,ls):
        for i in range(ls):
            j = i+ diff
            if j>=ls:
                break

            if s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1]
                if dp[i][j] == True:
                    lps = s[i:j+1]

    return lps



            





###### Testcases ######
# print(LPS("BABCBAB")) #output= BABCBAB
print(LPS("cbbd")) #output= bb
