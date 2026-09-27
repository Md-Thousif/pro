class Solution(object):
    def majorityElement(self, nums):
        m={}
        n=len(nums)
        ans=[]
        for i in range(0,len(nums)):
            if(nums[i] in m):
                m[nums[i]]+=1
            else:
                m[nums[i]]=1
        for i in m:
            if m[i]>(n/3):
                ans.append(i)
        return ans

        