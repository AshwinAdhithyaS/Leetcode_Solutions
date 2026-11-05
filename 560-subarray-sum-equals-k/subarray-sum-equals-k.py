class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        cur=0
        seen={0:1}
        for x in nums:
            cur+=x
            count+=seen.get(cur-k,0)
            seen[cur]=seen.get(cur,0)+1
        return count