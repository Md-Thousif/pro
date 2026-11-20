class Solution:
    def minSubArrayLen(self, tar: int, nums: list[int]) -> int:
        count=0
        ans=0
        summ=0
        inx=0
        for i in range(0,len(nums)):
            summ+=nums[i]
            count+=1
            while(summ>=tar):
                if ans==0:
                    ans=count
                ans=min(ans,count)
                summ-=nums[inx]
                inx+=1
                count-=1
        return ans
                    
                
