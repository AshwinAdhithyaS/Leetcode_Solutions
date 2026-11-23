class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        lis=[x for a in nums for x in a]
        count=Counter(lis)
        res=[]
        for i,j in count.items():
            if j==len(nums):
                res.append(i)
        return sorted(res)