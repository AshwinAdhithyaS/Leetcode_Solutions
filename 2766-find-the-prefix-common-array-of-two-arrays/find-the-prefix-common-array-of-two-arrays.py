class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def prev(a):
            count=0
            for i in range(a+1):
                for j in range(a+1):
                    if A[i]==B[j]:
                        count+=1
            return count
        result=[0]*len(A)
        for i in range(len(A)):
            result[i]+=prev(i)
        return result
