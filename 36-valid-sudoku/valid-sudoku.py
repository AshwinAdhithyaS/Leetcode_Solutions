class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def box_check(i,j):
            res=[]
            for ki in range(i,i+3):
                for kj in range(j,j+3):
                    if board[ki][kj].isdigit():
                        res.append(board[ki][kj])
            return len(set(res))==len(res)
        for i in range(9):
            row=set()
            col=set()
            for j in range(9):
                if i%3==0 and j%3==0:
                    if not box_check(i,j):
                        return False
                if board[i][j].isdigit():
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        return False
                if board[j][i].isdigit():
                    if board[j][i] not in col:
                        col.add(board[j][i])
                    else:
                        return False
        return True 