class Solution:
    def mostCommonWord(self, p: str, banned: list[str]) -> str:
        para=''
        for i in p:
            if i.isalpha() or i==' ':
                para+=i.lower()
            else:
                para+=' '
        lis=para.split()
        counts=Counter(lis)
        res=counts.most_common()
        for a in res:
            if a[0] not in banned:
                return a[0]