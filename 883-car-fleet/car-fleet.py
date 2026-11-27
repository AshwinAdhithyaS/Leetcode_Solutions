class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        disc={}
        for i in range(len(speed)):
            disc[position[i]]=speed[i]
        sor=dict(sorted(disc.items()))
        lis=[]
        for pos in sor:
            lis.append((target-pos)/sor[pos])
        count=0
        ahead=0
        for t in reversed(lis):
            if t>ahead:
                count+=1
                ahead=t
        return count