class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        out=True
        for i in range(len(s)-1):
            if abs(int(s[i])-int(s[i+1]))>2:
                out=False
                break
        return out
