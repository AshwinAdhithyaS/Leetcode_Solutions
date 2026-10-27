class Solution:
    def maximum69Number (self, num: int) -> int:
        lis=[x for x in str(num)]
        for i in range(len(lis)):
            if lis[i]=='6':
                lis[i]='9'
                break
        return int(''.join(lis))