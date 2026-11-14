class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        if len(word)<2:
            if word.isdigit():
                return 1
            else:
                return 0
        lis=[]
        dup_word=''
        for i in range(len(word)):
            if not word[i].isdigit():
                dup_word+=' '
            else:
                dup_word+=word[i]
        lis=dup_word.split()
        new_lis=[int(x) for x in lis]
        count=0
        for i in range(len(new_lis)):
            if new_lis[i] not in new_lis[:i]:
                count+=1
        return count