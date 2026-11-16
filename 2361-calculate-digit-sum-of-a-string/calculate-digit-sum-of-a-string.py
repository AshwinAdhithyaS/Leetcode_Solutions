class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def spliter(n):
            summ=''
            for i in range(0,len(s),k):
                temp=0
                for d in s[i:i+k]:
                    temp+=int(d)
                summ+=str(temp)
            return ''.join(summ)
        
        while len(s)>k:
            s=spliter(s)
        return s
        
