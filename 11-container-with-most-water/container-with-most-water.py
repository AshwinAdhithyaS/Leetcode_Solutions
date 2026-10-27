class Solution:
    def maxArea(self, height: list[int]) -> int:
        lef,rig=0,len(height)-1
        ma=0
        while lef<rig:
            base=rig-lef
            ma=max(ma,base*min(height[lef],height[rig]))
            if height[lef]<height[rig]:
                lef+=1
            else:
                rig-=1
        return ma