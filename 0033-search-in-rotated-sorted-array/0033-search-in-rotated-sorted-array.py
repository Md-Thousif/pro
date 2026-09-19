class Solution(object):
    def search(self, nums, tar):
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=i+(j-i)//2
            if(nums[mid]==tar):
                return mid
            if(nums[i]<=nums[mid]):
                if(nums[mid]>tar and nums[i]<=tar):
                    j=mid-1
                else:
                    i=mid+1
            if(nums[j]>=nums[mid]):
                if(nums[j]>=tar>nums[mid]):
                    i=mid+1
                else:
                    j=mid-1
        return -1

       

        