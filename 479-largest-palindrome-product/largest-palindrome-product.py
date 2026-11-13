class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n==1:
            return 9
        larg=0
        top=10**n-1
        for num1 in range(10**n-1,10**(n-1)-1,-1):
            s=str(num1)
            prod=int(s+s[::-1])
            i=top
            while i*i>=prod:
                if prod%i==0:
                    return prod%1337
                i-=1
        return -1