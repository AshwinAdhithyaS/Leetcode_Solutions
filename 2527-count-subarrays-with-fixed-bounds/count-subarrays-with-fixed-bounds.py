class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count=0
        bad=l_min=l_max=-1
        for i,x in enumerate(nums):
            if x < minK or x > maxK:
                bad=i
            if x==minK:
                l_min=i
            if x==maxK:
                l_max=i
            count+=max(0,min(l_min,l_max)-bad)
        return count
