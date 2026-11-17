class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n=nums.count(pivot)
        sol=[]
        result=[pivot]*n
        for i in nums:
            if i<pivot:
                sol.append(i)
            elif i>pivot:
                result.append(i)
        return sol+result
        