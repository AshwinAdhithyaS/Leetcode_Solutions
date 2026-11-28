class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        sol=''
        dic=dict(sorted(count.items(),key=operator.itemgetter(1),reverse=True))
        for a,b in dic.items():
            sol+=a*b
        return sol