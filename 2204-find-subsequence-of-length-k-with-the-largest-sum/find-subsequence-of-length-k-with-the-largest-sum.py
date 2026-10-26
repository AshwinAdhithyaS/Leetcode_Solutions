class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        nums_sort=sorted(nums)
        sol_lis=[]
        result=[]
        right,left=0,-1
        summ=0
        for i in range(k):
            lsum=summ+nums_sort[left]
            rsum=summ+nums_sort[right]
            if lsum>rsum:
                summ=lsum
                sol_lis.append(nums_sort[left])
                left-=1
            elif lsum<=rsum:
                summ=rsum
                sol_lis.append(nums_sort[right])
                right+=1
        for i in nums:
            if i in sol_lis:
                result.append(i)
                sol_lis.remove(i)
        return result
        