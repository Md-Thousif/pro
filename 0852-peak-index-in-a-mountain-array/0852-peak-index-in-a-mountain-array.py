class Solution(object):
    def peakIndexInMountainArray(self, arr):
        low=1
        high=len(arr)-2
        while(low<=high):
            mid=low+(high-low)//2
            if(arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid-1]>arr[mid]):
                high=mid-1
            else:
                low=mid+1