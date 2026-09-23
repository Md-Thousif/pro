class Solution(object):
    def minEatingSpeed(self, piles, h):
        ans1=0
        low=1
        high=max(piles)
        mid=0
        def ser():
            count=0
            for i in range(0,len(piles)):
                count+=(piles[i] + mid - 1) // mid
            return count
        while(low<=high):
            mid=low+(high-low)//2
            ans=ser()
            if(ans<=h):
                ans1=mid
                high=mid-1
            elif(ans>h):
                low=mid+1    
        return ans1