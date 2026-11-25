class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack=[]
        for i in range(1,n+1):
            stack.append('Push')
            if i!=target[0]:
                stack.append('Pop')
            else:
                target.pop(0)
                if target==[]:
                    break
        return stack