class Solution(object):
    def longestOnes(self, nums, k):
        left=0
        ans=0
        count=0
        euq=0
        for i in range(0,len(nums)):
                count+=1
                if(nums[i]==0):
                    euq+=1
                    while(euq>k):
                        if(nums[left]==0):
                            euq-=1
                        count-=1
                        left+=1
                ans=max(ans,count)
        return ans
