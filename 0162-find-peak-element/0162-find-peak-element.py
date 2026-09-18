class Solution(object):
    def findPeakElement(self, nums):
        low=0
        h=len(nums)-1
        while(low<h):
            mid=low+(h-low)//2
            if(nums[mid]>nums[mid+1]):
                h=mid
            else:
                low=mid+1
        return low