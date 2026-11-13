class Solution:
    def trap(self, height: list[int]) -> int:
        n=len(height)
        if n<=2:
            return 0
        l_max=[0]*n
        r_max=[0]*n
        l_max[0]=height[0]
        for i in range(1,n):
            l_max[i]=max(l_max[i-1],height[i])
        
        r_max[n-1]=height[n-1]
        for j in range(n-2,-1,-1):
            r_max[j]=max(r_max[j+1],height[j])
        water=0
        for i in range(1,len(height)-1):
            water+=max(0,min(l_max[i],r_max[i])-height[i])
        return water