class Solution:
    def countAndSay(self, n: int) -> str:
        def count_and_say(n1,st1):
            if n1==0:
                return '1'
            l=len(st1)
            res=''
            st=0
            while st<l:
                count=1
                while st<l-1 and st1[st]==st1[st+1]:
                    count+=1
                    st+=1
                res+=str(count)+st1[st]
                st+=1
            return res

        sol=''
        for i in range(n):
            sol=count_and_say(i,sol)
        return sol