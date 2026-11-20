class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(arr,low,mid,high):
            temp=[]
            left,right=low,mid+1
            while left<=mid and right<=high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    right+=1
            
            while (left<=mid):
                temp.append(arr[left])
                left+=1
            while (right<=high):
                temp.append(arr[right])
                right+=1
            
            for i in range(low,high+1):
                arr[i]=temp[i-low]
        
        def ms(arr,low,high):
            if (low>=high):
                return 
            mid=(low+high)//2
            ms(arr,low,mid)
            ms(arr,mid+1,high)
            merge(arr,low,mid,high)
        ms(nums,0,len(nums)-1)
        return nums
            
