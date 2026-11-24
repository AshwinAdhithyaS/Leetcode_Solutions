class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        digi=str(digit)
        count=0
        for i in nums:
            count+=str(i).count(digi)
        return count