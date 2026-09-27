class Solution(object):
    def heightChecker(self, heights):
        num=sorted(heights)
        c=0
        for i in range(0,len(heights)):
            if(num[i]!=heights[i]):
                c+=1 
        return c