class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        if len(nums)==0:
            return [[]]
        perm=self.permuteUnique(nums[1:])
        res=[]
        for p in perm:
            for i in range(len(nums)):
                p_copy=p.copy()
                p_copy.insert(i,nums[0])
                if p_copy not in res:
                    res.append(p_copy)
        return res