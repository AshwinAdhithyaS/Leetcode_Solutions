class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count=0 
        run=0
        for x in nums:
            if minK <= x <= maxK:
                run+=1
                count+=run
            else:
                run=0
        return count