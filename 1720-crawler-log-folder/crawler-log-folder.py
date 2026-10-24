class Solution:
    def minOperations(self, logs: list[str]) -> int:
        coun=0
        for i in logs:
            if i=='../':
                if coun >0:
                    coun-=1
            elif i=='./':
                continue
            else:
                coun+=1
        return coun