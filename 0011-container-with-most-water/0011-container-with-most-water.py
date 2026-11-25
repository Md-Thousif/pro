class Solution:
    def maxArea(self, h: list[int]) -> int:
        i=0
        j=len(h)-1
        ans=0
        while(i<j):
            width=j-i
            hei=min(h[i],h[j])
            area=width*hei
            ans=max(area,ans)
            if h[i]>h[j]:
                j-=1
            else:
                i+=1
        return ans