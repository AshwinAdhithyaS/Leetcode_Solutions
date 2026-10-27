class Solution:
    def maxArea(self, height: list[int]) -> int:
        lef=0
        ma=0
        rig=len(height)-1
        while lef<rig:
            ma=max(ma,(rig-lef)*min(height[lef],height[rig]))
            if height[lef]<height[rig]:
                lef+=1
            else:
                rig-=1
        return ma