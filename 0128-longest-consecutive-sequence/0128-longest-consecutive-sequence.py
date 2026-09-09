class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        ans=0
        for x in s:
            if(x-1 not in s):
                c=1
                while x+c in s:
                    c+=1
                ans=max(ans,c)
        return ans


