class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        down=len(board)
        right=len(board[0])

        def check(a,b,i):
            if i==len(word):
                return True
            if not(0<=a<down and 0<=b<right) or board[a][b]!=word[i]:
                return False
            temp=board[a][b]
            board[a][b]='#'
            found=(check(a+1,b,i+1) or check(a,b+1,i+1) or check(a-1,b,i+1) or check(a,b-1,i+1))
            board[a][b]=temp
            return found

        for i in range(down):
            for j in range(right):
                if check(i,j,0):
                    return True
        return False
