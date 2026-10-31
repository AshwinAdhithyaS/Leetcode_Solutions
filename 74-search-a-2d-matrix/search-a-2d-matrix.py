class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row=-1
        top_row=0
        bottom_row=len(matrix)-1
        while top_row<=bottom_row:
            mid_row=(top_row+bottom_row)//2
            if matrix[mid_row][0]<=target<=matrix[mid_row][-1]:
                row=mid_row
                break
            elif matrix[mid_row][-1]<target:
                top_row=mid_row+1
            else:
                bottom_row=mid_row-1
        if row==-1:
            return False
        hi,lo=0,len(matrix[0])-1
        lis=matrix[row]
        while hi<=lo:
            mid=(hi+lo)//2
            if lis[mid]==target:
                return True
            elif lis[mid]<target:
                hi=mid+1
            else:
                lo=mid-1
        return False