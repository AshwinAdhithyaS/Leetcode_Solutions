class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minsum=float('inf')
        for i,a in enumerate(nums):
            lis=[a]
            if l==1:
                if a>0:
                    minsum=min(minsum,a)
            for b in nums[i+1:]:
                lis.append(b)
                if l<=len(lis)<=r:
                    if sum(lis)>0:
                        minsum=min(sum(lis),minsum)
                elif len(lis)>r:
                    break
        if minsum==float('inf'):
            return -1
        return minsum 
                   