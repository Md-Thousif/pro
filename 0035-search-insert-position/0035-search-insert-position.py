class Solution:
    def searchInsert(self, nums: list[int], tar: int) -> int:
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=i+(j-i)//2
            if nums[mid]==tar:
                return mid
            elif nums[mid]<tar:
                i=mid+1
            else:
                j=mid-1
        return i