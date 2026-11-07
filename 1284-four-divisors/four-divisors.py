class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def div_coun(n):
            cnt,summ=0,0
            i=1
            while i*i<=n:
                if n%i==0:
                    j=n//i
                    if j==i:
                        cnt+=1
                        summ+=j
                    else:
                        cnt+=2
                        summ+=i+j
                    if cnt>4:
                        return 0
                i+=1
            return summ if cnt==4 else 0
        return sum(div_coun(x) for x in nums)
