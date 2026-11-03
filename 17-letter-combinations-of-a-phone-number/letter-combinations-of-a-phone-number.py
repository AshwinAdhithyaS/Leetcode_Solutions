class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==1:
            sol=[]
            for i in dic[digits]:
                sol.append(i)
            return sol
        elif len(digits)==2:
            sol=[]
            for i in dic[digits[0]]:
                for j in dic[digits[1]]:
                    sol.append(i+j)
            return sol
        elif len(digits)==3:
            sol=[]
            for i in dic[digits[0]]:
                for j in dic[digits[1]]:
                    for k in dic[digits[2]]:
                        sol.append(i+j+k)
            return sol
        elif len(digits)==4:
            sol=[]
            for i in dic[digits[0]]:
                for j in dic[digits[1]]:
                    for k in dic[digits[2]]:
                        for l in dic[digits[3]]:
                            sol.append(i+j+k+l)
            return sol