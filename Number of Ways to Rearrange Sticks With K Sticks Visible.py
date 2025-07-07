def rearrangeSticks(n, k):
        MOD=10**9+7
        dp=[[0]*(k+1) for _ in range(n+1)]
        if k==n or k==1:
            return 1
        for i in range(1,n+1):
            dp[i][1]=1
        for i in range(1,n+1):
            for j in range(2,min(k,i)+1):
                dp[i][j] = dp[i - 1][j - 1]+ (i - 1) * dp[i - 1][j]
         
        print(dp)
        return dp[n][k]%MOD
print(rearrangeSticks(5,3))

