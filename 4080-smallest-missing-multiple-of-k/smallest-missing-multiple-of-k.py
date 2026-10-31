class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        non_dup=set(nums)
        check=k
        while check in non_dup:
            check+=k
        return check