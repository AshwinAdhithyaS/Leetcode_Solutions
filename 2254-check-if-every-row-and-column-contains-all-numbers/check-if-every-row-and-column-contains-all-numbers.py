class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n=len(matrix)
        for i in range(n):
            row_set=set(matrix[i])
            col_set=set()
            if len(row_set)!=n:
                return False
            for j in range(n):
                col_set.add(matrix[j][i])
            if len(col_set)!=n:
                return False
        return True
