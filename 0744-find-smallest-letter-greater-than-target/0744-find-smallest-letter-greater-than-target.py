class Solution(object):
    def nextGreatestLetter(self, let, tar):
        ans=let[0]
        low=0
        high=len(let)-1
        while(low<=high):
            mid=low+(high-low)//2
            if(let[mid]>tar):
                ans=let[mid]
                high=mid-1
            else:
                low=mid+1
        return ans
            

        