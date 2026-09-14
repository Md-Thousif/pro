class Solution(object):
    def minSubArrayLen(self, tar, nums):
        c=0
        summ=0
        ans=0
        inn=0
        for i in range(0,len(nums)):
            summ+=nums[i]
            c+=1
            while(summ>=tar):
                if(ans==0):
                    ans=c
                ans=min(ans,c)
                summ-=nums[inn]
                inn+=1
                c-=1
        return ans
                

        