def longestIncreasingPath(matrix) -> int:
    n=len(matrix)
    m=len(matrix[0])
    dp=[[-1]*m for _ in range(n)]
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        

    def f(i,j):
        if dp[i][j]!=-1:
            return dp[i][j]
        max_len=1
        for dx, dy in dir:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m:
                if matrix[ni][nj] < matrix[i][j]:
                    max_len=max(max_len,1+f(ni,nj))
        dp[i][j]=max_len
        return dp[i][j]
    
    
    maxi=-1      
    for i in range(n):
        for j in range(m):
            maxi=max(maxi,f(i,j)) 
    print(dp) 
    return maxi
print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))