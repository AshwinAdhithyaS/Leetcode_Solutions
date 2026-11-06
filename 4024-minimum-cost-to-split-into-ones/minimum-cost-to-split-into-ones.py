class Solution:
    def minCost(self, n: int) -> int:
        cost=sum(x for x in range((n-1),0,-1))
        return cost