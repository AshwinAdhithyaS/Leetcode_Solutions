class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        res = set(nums)
        ma = 0
        for num in res:
            if num - 1 not in res:
                temp_ma = 1
                while num + temp_ma in res:
                    temp_ma += 1
                ma = max(ma, temp_ma)
        return ma