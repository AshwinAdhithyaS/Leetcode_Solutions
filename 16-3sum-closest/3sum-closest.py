class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        close=float('inf')
        n=len(nums)
        for i in range(n-2):
            lo=i+1
            hi=n-1
            while lo<hi:
                current=nums[i]+nums[lo]+nums[hi]
                if current==target:
                    return current
                if abs(target-current)<abs(target-close):
                    close=current
                if current<target:
                    lo+=1
                else:
                    hi-=1
        return close
