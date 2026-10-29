class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic={}
        for s in strs:
            str1=''.join(sorted(s))
            if str1 in dic:
                dic[str1].append(s)
            else:
                dic[str1]=[s]
        return list(dic.values())
                
