class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        lar=nums[0]
        pres=0
        for n in nums:
            pres+=n
            lar=max(lar,pres)
            if pres<0:
                pres=0
        return lar