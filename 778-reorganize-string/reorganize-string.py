class Solution:
    def reorganizeString(self, s: str) -> str:
        counts=Counter(s)
        n=len(s)
        ma=max(counts.values())
        if ma>(n+1)//2:
            return ''
        sol=['']*n
        st=0
        for a,b in counts.most_common():
            for _ in range(b):
                if st >= n:
                     st=1
                sol[st]=a
                st+=2
        
        return ''.join(sol)