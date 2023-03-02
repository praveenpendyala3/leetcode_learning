
def minPathSum(grid):
    m = len(grid) # number of rows
    n = len(grid[0]) # number of columns
    
    maxsum = 100*(m+n) # Absolute Maximum sum thats not possible based on constrains to move from top left to bottom right.

    # dp = [[-1 for _ in range(n)] for _ in range(m)] # dp array 

    def minMove(i,j):           
        
        if i==0 and j==0:
            # dp[0][0]  = grid[0][0]
            return grid[0][0]

        # if dp[i][j] != -1:
        #     return dp[i][j]

        s1 = grid[i][j] + minMove(i-1,j) if i>=1 else maxsum #Move up
        s2 = grid[i][j] + minMove(i,j-1) if j>=1 else maxsum #move left

        return min(s1,s2)

        # dp[i][j] = min(s1,s2)
        # return dp[i][j]


    return minMove(m-1,n-1)


###### Testcases ######
ip = [[1,3,1],[1,5,1],[4,2,1]] #ans = 7
ip = [[1,2,3],[4,5,6]] #ans =12
print(minPathSum(ip))
