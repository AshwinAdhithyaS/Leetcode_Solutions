class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        lis=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    lis[i][j]=1
                else:
                    left=lis[i][j-1] if j>0 else 0
                    up=lis[i-1][j] if i>0 else 0
                    if i==0 and left==1:
                        lis[i][j]=1
                    elif j==n-1 and up==1:
                        lis[i][j]=1
        
        result=[]
        for i in lis:
            st=''
            for j in i:
                if j==1:
                    st+='.'
                else:
                    st+='#'
            result.append(st)
        return result
                