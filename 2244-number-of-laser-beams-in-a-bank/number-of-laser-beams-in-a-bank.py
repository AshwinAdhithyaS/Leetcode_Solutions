class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        count=0
        for i in range(len(bank)-1):
            coun=bank[i].count('1')
            for j in range(i+1,len(bank)):
                count+=coun*bank[j].count('1')
                if bank[j].count('1') > 0:
                    break
        return count

                