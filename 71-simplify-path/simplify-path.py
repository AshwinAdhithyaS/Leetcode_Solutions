class Solution:
    def simplifyPath(self, path: str) -> str:
        res=path.split('/')
        sol=[]
        for i in res:
            if i=='' or i=='.':
                continue
            elif i=='..':
                if sol:
                    sol.pop()
            else:
                sol.append(i)
        return '/'+'/'.join(sol)