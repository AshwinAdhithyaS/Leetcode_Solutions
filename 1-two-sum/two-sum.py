class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        for i in range(0,len(nums)+1):
            x=target-nums[i]
            if x in map:
                return [i,map[x]]
            else:
                map[nums[i]]=i

            