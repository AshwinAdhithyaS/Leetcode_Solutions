class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n=len(grid)-1
        m=len(grid[0])-1
        summ=[[0]*(m+1) for x in range(n+1)]
        for down in range(n+1):
            for left in range(m+1):
                if down==0 and left==0:
                    summ[down][left]=0+grid[down][left]
                elif down==0:
                    summ[down][left]=summ[down][left-1]+grid[down][left]
                elif left==0:
                    summ[down][left]=summ[down-1][left]+grid[down][left]
                else:
                    summ[down][left]=min(summ[down-1][left],summ[down][left-1])+grid[down][left]

        return summ[n][m]
