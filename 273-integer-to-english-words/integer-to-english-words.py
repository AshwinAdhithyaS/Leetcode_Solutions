class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return 'Zero'

        below_20=["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens=["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousand=["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n==0:
                return ''
            elif n<20:
                return below_20[n]+' '
            elif n<100:
                return tens[n//10]+' '+helper(n%10)
            else:
                return below_20[n//100]+' Hundred '+helper(n%100)
        res=''
        i=0
        while num>0:
            chunk=num%1000
            if chunk!=0:
                res=helper(chunk)+thousand[i]+' '+res
            i+=1
            num=num//1000
        
        return res.strip()




            