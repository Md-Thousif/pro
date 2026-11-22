class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        i=0
        j=len(arr)-1
        while(i<j):
            mid=i+(j-i)//2
            if arr[mid]>arr[mid+1]:
                ans=mid
                j=mid
            else:
                i=mid
            if arr[mid]>arr[mid-1]:
                ans=mid
                i=mid
            else:
                j=mid
        return ans
            
