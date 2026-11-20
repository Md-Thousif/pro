class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        i=0
        j=len(nums)-1
        while(i<j):
            mid=i+(j-i)//2
            if(nums[mid]>nums[mid+1] ):
                j=mid
            elif(nums[mid]<nums[mid+1]):
                i=mid+1
        return j
