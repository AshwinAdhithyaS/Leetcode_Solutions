class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        fir_ele=[]
        for i in nums:
            fir_ele.append(int(str(i)[0]))
        
        def arrange(fir_ele,ma,out):
            best=-1
            for i,x in enumerate(fir_ele):
                if x==ma:
                    if best==-1:
                        best=i
                    else:
                        a,b=str(nums[i]),str(nums[best])
                        if a+b>b+a:
                            best=i
            out+=str(nums[best])
            fir_ele[best]=-1
            return out 
        lis=sorted(fir_ele)
        outi=''
        for numm in lis[::-1]:
            outi=arrange(fir_ele,numm,outi)

        if outi[0]=='0':
            return '0'
        return outi
