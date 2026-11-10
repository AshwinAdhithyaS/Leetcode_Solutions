class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            k=1
            while k*k<=i:
                dp[i]=min(dp[i],dp[i-k*k]+1)
                k+=1
        return dp[n]