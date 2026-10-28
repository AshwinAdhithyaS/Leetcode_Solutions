class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bin(x):
            lo,hi=0,len(nums)
            while lo<hi:
                mid=(lo+hi)//2
                if nums[mid]<x:
                    lo=mid+1
                else:
                    hi=mid
            return lo
        lef=bin(target)
        if lef==len(nums) or nums[lef]!=target:
            return [-1,-1]
        rig=bin(target+1)-1
        return [lef,rig]