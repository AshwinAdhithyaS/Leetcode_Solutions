class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9+7
        n=len(arr)
        summ=0
        p=[0]
        for i,x in enumerate(arr):
            summ+=x
            p.append(summ)
        odd,even=0,0
        for v in p:
            if v%2==0:
                even+=1
            else:
                odd+=1
        return (odd*even)%mod
        
