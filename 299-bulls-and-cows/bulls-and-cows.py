class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secretdic=Counter(secret)
        print(secretdic)
        cowc,bullc=0,0
        for i in range(len(guess)):
            bullc+=int(secret[i]==guess[i])
        for j in set(secret):
            cowc+=min(secret.count(j),guess.count(j))
        return str(bullc)+'A'+str(cowc-bullc)+'B'