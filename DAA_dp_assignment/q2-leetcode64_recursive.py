
def minPathSum(grid):
    m = len(grid) # number of rows
    n = len(grid[0]) # number of columns
    
    maxsum = 100*(m+n) # Absolute Maximum sum thats not possible based on constrains to move from top left to bottom right.


    ## DEFINITION: 
    # minMove(i,j) = minimum sum to reach i,j in the matrix. 

    # minMove(i,j) = min(s1,s2);
    # s1 = grid[i][j] + minMove(i-1,j)      # if we reach i,j by moving down
    # s2 = grid[i][j] + minMove(i,j-1)      # If we reach i,j by move left


    def minMove(i,j):           
        if i==0 and j==0:
            return grid[0][0]


        s1 = grid[i][j] + minMove(i-1,j) if i>=1 else maxsum #Move up
        s2 = grid[i][j] + minMove(i,j-1) if j>=1 else maxsum #move left

        return min(s1,s2)

    return minMove(m-1,n-1)


###### Testcases ######
ip = [[1,3,1],[1,5,1],[4,2,1]] #ans = 7
ip = [[1,2,3],[4,5,6]] #ans =12
print(minPathSum(ip))
