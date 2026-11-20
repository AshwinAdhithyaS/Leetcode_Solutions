class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretdic=Counter(secret)
        print(secretdic)
        cowc,bullc=0,0
        for i in range(len(guess)):
            if guess[i] in secretdic and secretdic[guess[i]]!=0:
                if guess[i]==secret[i]:
                    bullc+=1
                    secretdic[guess[i]]-=1
        for i in range(len(guess)):
            if guess[i] in secretdic and secretdic[guess[i]]!=0:
                if guess[i]!=secret[i]:
                    cowc+=1
                    secretdic[guess[i]]-=1
        return str(bullc)+'A'+str(cowc)+'B'