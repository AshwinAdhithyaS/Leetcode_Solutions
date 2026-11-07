class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        lar=nums[0]
        pres=0
        for n in nums:
            pres+=n
            lar=pres if pres > lar else lar
            if pres<0:
                pres=0
        return lar