class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        exp=1
        for x in nums:
            if x==exp:
                exp+=1
            elif exp<x:
                break
        return exp