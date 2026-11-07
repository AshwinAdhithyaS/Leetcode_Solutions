class Solution:
    def candy(self, ratings: list[int]) -> int:
        n=len(ratings)
        candies=[1]*n

        for lef in range(1,n):
            if ratings[lef]>ratings[lef-1]:
                candies[lef]=candies[lef-1]+1
        
        for rig in range(n-2,-1,-1):
            if ratings[rig]>ratings[rig+1]:
                candies[rig]=max(candies[rig],candies[rig+1]+1)
        return sum(candies)