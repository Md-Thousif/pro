class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i=1
        j=max(piles)
        mid=0
        ans2=0
        def num():
            count=0
            for i in range(len(piles)):
                count+=(piles[i] + mid -1)//mid
            return count

        while(i<=j):
            mid=i+(j-i)//2
            ans=num()
            if ans<=h:
                ans2=mid
                j=mid-1
            elif ans>h:
                i=mid+1
        return ans2