class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps=0
        nums.sort()
        mis=nums[len(nums)//2]
        for i in nums:
            steps+=abs(mis-i)
        return steps
        