class Solution:
    def minMoves(self, nums: list[int]) -> int:
        step=0
        m=min(nums)
        for x in nums:
            step+=x-m
        return step
        