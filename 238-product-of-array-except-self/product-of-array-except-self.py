import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        if 0 in nums:
            res=[0]*n
            if nums.count(0)==1:
                indi=nums.index(0)
                nums.remove(0)
                res[indi]=math.prod(nums)
            return res
        prod=math.prod(nums)
        return [prod//x for x in nums]