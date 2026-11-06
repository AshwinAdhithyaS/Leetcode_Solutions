class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        if n==0:
            return []
        res=[1]*n
        right=1
        for x in range(n):
            res[x]=right
            right*=nums[x]
        left=1
        for x in range(n-1,-1,-1):
            res[x]*=left
            left*=nums[x]
        return res