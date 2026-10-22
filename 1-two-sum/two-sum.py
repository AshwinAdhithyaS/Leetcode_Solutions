class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)+1):
            x=nums[i]
            for k in range(i+1,len(nums)):
                j=nums[k]
                if x+j == target:
                    return i,k
                    break