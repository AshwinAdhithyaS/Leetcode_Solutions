class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def st_inc(i):
            count=1
            while i < len(nums) - 1 and nums[i] < nums[i + 1]:
                count += 1
                i += 1
            return count
        def st_dec(i):
            count=1
            while i < len(nums) - 1 and nums[i] > nums[i + 1]:
                count += 1
                i += 1
            return count

        ma=0
        i=0
        for i in range(len(nums)):
            ma=max(ma,st_inc(i),st_dec(i))
        return ma
                
