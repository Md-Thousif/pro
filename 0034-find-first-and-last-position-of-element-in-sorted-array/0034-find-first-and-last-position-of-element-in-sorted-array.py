class Solution(object):
    def searchRange(self, nums, tar):
        def first():
            ans1=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=low+(high-low)//2
                if(nums[mid]==tar):
                    ans1=mid
                    high=mid-1
                elif(nums[mid]<tar):
                    low=mid+1
                else:
                    high=mid-1
            return ans1
        def last():
            ans2=-1
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=low+(high-low)//2
                if(nums[mid]==tar):
                    ans2=mid
                    low=mid+1
                elif(nums[mid]<tar):
                    low=mid+1
                else:
                    high=mid-1
            return ans2
        return first(),last()
