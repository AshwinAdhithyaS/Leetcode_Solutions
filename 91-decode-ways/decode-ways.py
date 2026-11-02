class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        prev1,prev2=1,1
        for i in range(1,len(s)):
            cur=0
            si= s[i]!='0'
            pa=10<=int(s[i-1:i+1])<=26
            if si:
                cur+=prev1
            if pa:
                cur+=prev2
            prev1,prev2=cur,prev1
        return prev1