class Solution(object):
    def targetIndices(self, nums, tar):
        nums=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            if(nums[i]==tar):
                ans.append(i)
        return ans    