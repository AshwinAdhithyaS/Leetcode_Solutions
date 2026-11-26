class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove=10
        at=True
        while n >= remove:
            n-=remove
            remove-=1
            at=not at
        return not at