class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        res=nums[0]
        tot=nums[0]
        for i in range(1,len(nums)):
            tot+=nums[i]
            res=max(res,math.ceil(tot/(i+1)))
        return res