import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        if math.prod(nums)==math.gcd(*nums)*math.lcm(*nums):
            return len(nums)
        else:
            ma=0
            for i in range(len(nums)):
                for j in range(len(nums)-1,i-1,-1):
                    if math.prod(nums[i:j+1])==math.lcm(*nums[i:j+1])*math.gcd(*nums[i:j+1]):
                        ma=max(ma,len(nums[i:j+1]))
            return ma