import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        ans=[]
        a=0
        b=0
        for i in range(0,len(stones)):
            heapq.heappush(ans,-stones[i])
        while(len(ans)>1):
            a=-heapq.heappop(ans)
            b=-heapq.heappop(ans)
            if(a!=b):
                heapq.heappush(ans,-(a-b))
        if ans:
            return -ans[0]
            
        return 0
        
        

        