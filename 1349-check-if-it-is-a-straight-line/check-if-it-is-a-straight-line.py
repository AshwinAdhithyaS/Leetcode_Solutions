class Solution:
    def checkStraightLine(self, c: list[list[int]]) -> bool:
        a,b=c[0],c[-1]
        for i in range(1,len(c)-1):
            if (b[0]-a[0])*(c[i][1]-a[1])-(b[1]-a[1])*(c[i][0]-a[0])!=0:
                return False
        return True
                