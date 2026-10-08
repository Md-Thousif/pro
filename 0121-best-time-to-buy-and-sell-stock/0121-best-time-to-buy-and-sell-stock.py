class Solution(object):
    def maxProfit(self, p):
        buy=p[0]
        best=0
        for i in range (1,len(p)):
            if p[i]<buy:
                buy=p[i]
            else:
                best=max(p[i]-buy,best)
        return best
            