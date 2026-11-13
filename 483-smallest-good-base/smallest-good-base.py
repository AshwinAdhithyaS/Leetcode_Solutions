import math
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n=int(n)
        max_m=int(math.log2(int(n)+1))

        def calculate(m,k,n):
            total=1
            current=1
            for i in range(m-1):
                current*=k
                if current>n:
                    return n+1
                total+=current
                if total>n:
                    return n+1
            return total

        for m in range(max_m,1,-1):
            lo=2
            hi=int(n**(1/(m-1)))+1
            while lo<=hi:
                mid=(lo+hi)//2
                tot=calculate(m,mid,n)
                if tot==n:
                    return str(mid)
                elif tot<n:
                    lo=mid+1
                else:
                    hi=mid-1
        return str(n-1)