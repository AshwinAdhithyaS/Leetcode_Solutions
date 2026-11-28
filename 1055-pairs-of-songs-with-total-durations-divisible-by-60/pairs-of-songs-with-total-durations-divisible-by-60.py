class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        rem=[0]*60
        count=0
        for x in time:
            r=x%60
            count+=rem[(60-r)%60]
            rem[r]+=1
        return count