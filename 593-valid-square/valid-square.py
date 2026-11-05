class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        def dis(a,b):
            return (a[0]-b[0])**2+(a[1]-b[1])**2
        d=sorted([dis(p1,p2),dis(p2,p3),dis(p3,p4),dis(p4,p1),dis(p2,p4),dis(p1,p3)])
        return d[0]>0 and d[0]==d[1]==d[2]==d[3] and d[4]==d[5]==d[0]*2 
        