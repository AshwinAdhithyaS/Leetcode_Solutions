class Solution:
    def canJump(self, nums: list[int]) -> bool:
        out=False
        reach=0
        indi=0
        while indi<=len(nums)-1 and indi<=reach:
            reach=max(reach,indi+nums[indi])
            if reach>=len(nums)-1:
                out=True
                break
            indi+=1
        return out