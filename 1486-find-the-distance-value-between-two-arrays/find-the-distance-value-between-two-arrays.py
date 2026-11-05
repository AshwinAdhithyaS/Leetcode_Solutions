class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        def check(n):
            for k in arr2:
                if abs(k-n)<=d:
                    return False
            return True
        coun=0
        for i in arr1:
            if check(i):
                coun+=1
        return coun