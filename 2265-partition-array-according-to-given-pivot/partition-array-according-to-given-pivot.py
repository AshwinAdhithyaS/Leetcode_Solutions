class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less,equal,greater=[],[],[]
        for i in nums:
            if pivot>i:less.append(i)
            if pivot==i:equal.append(i)
            if pivot<i:greater.append(i)
        return less+equal+greater
        