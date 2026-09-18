class Solution(object):
    def searchInsert(self, nums, tar):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=low+(high-low)//2
            if(nums[mid]==tar):
                return mid
            elif(nums[mid]>tar):
                high=mid-1
            elif(nums[mid]<tar):
                low=mid+1
        return low