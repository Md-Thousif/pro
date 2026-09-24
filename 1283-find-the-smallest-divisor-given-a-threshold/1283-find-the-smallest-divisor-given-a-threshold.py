class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        mid=0
        def ans():
            count=0
            for i in range(0,len(nums)):
                count+=(mid+nums[i]-1)//mid
            return count
        while(low<=high):
            mid=low+(high-low)//2
            check=ans()
            if(check<=threshold):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
        