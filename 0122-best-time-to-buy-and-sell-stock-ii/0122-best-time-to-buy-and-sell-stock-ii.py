class Solution(object):
    def maxProfit(self, p):
        ans=0
        buy=p[0]
        i=1
        while i<len(p):
            if p[i]<buy:
                buy=p[i]
                i+=1
            else:
                ans+=p[i]-buy
                buy=p[i]
                i+=1
        return ans
                

        