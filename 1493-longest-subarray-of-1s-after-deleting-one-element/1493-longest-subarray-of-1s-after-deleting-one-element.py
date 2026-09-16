class Solution(object):
    def longestSubarray(self, nums):
        count=0
        ans=0
        euq=0
        left=0
        for i in range(0,len(nums)):
            if(nums[i]==1):
                count+=1
            else:
                euq+=1
                while(euq>1):
                    if(nums[left]==0):
                        euq-=1
                    else:
                        count-=1
                    left+=1
            ans=max(ans,count)
        if(ans==len(nums)):
            return ans-1
        return ans