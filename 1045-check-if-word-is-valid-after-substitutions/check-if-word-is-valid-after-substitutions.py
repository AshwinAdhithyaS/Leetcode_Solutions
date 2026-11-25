class Solution:
    def isValid(self, s: str) -> bool:
        s2=''
        while s!=s2:
            s,s2=s.replace('abc',''),s
        return s==''