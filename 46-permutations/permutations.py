class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        if len(nums)<=1:
            return [nums]
        def combi(start):
            if start==len(nums):
                res.append(list(nums))
                return
            for i in range(start,len(nums)):
                nums[start],nums[i]=nums[i],nums[start]
                combi(start+1)
                nums[start],nums[i]=nums[i],nums[start]
        combi(0)
        return res