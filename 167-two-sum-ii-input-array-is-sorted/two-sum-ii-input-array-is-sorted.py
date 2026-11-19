class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        map={}
        for i in range(len(numbers)+1):
            x=target-numbers[i]
            if x in map:
                return sorted([i+1,map[x]+1])
            else:
                map[numbers[i]]=i