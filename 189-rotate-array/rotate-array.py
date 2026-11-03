class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        if k>=l:
            while k>=l:
                k-=l
        nums[:]=nums[l-k:]+nums[:l-k]