class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        count=0
        ans=0
        curr=0
        j=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]==0:
                count+=1
                curr+=1
                while(curr>k):
                    if nums[j]==0:
                        curr-=1
                    count-=1
                    j+=1
            ans=max(count,ans)
        return ans


