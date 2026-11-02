class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2,n-1):
            num=n
            digit=[]
            while num>0:
                digit.append(num%base)
                num=num/base
            if digits!=digits[::-1]:
                return False
        return True