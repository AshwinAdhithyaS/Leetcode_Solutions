class Solution:
    def minCost(self, n: int) -> int:
        cost=0
        while n>0:
            cost+=(n-1)
            n-=1
        return cost