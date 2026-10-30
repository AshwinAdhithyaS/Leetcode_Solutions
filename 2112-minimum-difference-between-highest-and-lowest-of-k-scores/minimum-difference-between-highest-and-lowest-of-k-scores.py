class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        def miscoun(indi,sub2):
            return min(sub2,nums[indi+k-1]-nums[indi])
        sub=nums[k-1]-nums[0]
        for i in range(1,len(nums)-k+1):
            sub=miscoun(i,sub)
        return sub