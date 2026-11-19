class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        tot=sorted(nums1+nums2)
        n=len(tot)
        if n%2==0:
            return (tot[n//2]+tot[n//2-1])/2
        else:
            return float(tot[n//2])