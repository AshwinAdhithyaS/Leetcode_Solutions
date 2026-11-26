class Solution:
    def removeStars(self, s: str) -> str:
        res=[]
        for i in s:
            res.append(i)
            if i=='*':
                res.pop()
                res.pop()
        return ''.join(res)