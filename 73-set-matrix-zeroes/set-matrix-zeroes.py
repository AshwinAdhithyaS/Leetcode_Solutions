class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros=[]
        for i,lis in enumerate(matrix):
            for ind,j in enumerate(lis):
                if j==0:
                    zeros.append((i,ind))
        for i,ind in zeros:
            matrix[i]=[0]*len(matrix[i])
            for k in range(0,len(matrix)):
                matrix[k][ind]=0 

