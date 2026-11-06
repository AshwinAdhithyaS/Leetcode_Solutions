from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq=Counter(nums)
        lis=[]
        for a,b in freq.most_common():
            lis.append(a)
            k-=1
            if k==0:
                break
        return lis
