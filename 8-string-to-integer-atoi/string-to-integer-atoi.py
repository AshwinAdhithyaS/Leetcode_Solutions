class Solution:
    def myAtoi(self, s: str) -> int:
        dic2={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        out=''
        sign=1
        s=s.lstrip()
        for i in range(len(s)):
            if i==0 and (s[i]=='-' or s[i]=='+'):
                if s[i]=='-':
                    sign=-1
            elif s[i] in dic2:
                out+=s[i]
            else:
                break
        if out=='':
            return 0
        res=0
        for ch in out:
            res=res*10+dic2[ch]
        res=res*sign
        if res > 2**31-1:
            return 2**31-1
        if res < -2**31:
            return -2**31
        return res
        

