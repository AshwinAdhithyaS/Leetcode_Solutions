class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        count=1
        for i in range(1,len(arr)):
            maxi=max(arr[:i])
            mini=min(arr[i:])
            if maxi<=mini:
                count+=1
        return count