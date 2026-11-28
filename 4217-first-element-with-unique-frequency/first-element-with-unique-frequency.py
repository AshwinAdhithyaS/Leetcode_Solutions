class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        counts=Counter(nums)
        freq_count=Counter(counts.values())
        for x in nums:
            if freq_count[counts[x]]==1:
                return x
        return -1
