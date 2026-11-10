class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev1,prev2=0,0
        for num in nums[1:]:
            current=max(prev1,prev2+num)
            prev2=prev1
            prev1=current
        prev3,prev4=0,0
        for num in nums[:-1]:
            current=max(prev3,prev4+num)
            prev4=prev3
            prev3=current
        return max(prev1,prev3)
        