class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count=0
        for i in range(num1,num2+1):
            if len(str(i))>=3:
                stri=str(i)
                for j in range(1,len(stri)-1):
                    if (stri[j]>stri[j-1] and stri[j]>stri[j+1]) or (stri[j]<stri[j-1] and stri[j]<stri[j+1]):
                        count+=1
        return count