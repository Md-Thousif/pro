import heapq
class Solution(object):
    def findRelativeRanks(self, score):
        ans=[""]*len(score)
        res=[]
        for i in range(0,len(score)):
            heapq.heappush(res,(-score[i],i))
        rank=1
        while res:
            neg,indx=heapq.heappop(res)
            if rank==1:
                ans[indx]="Gold Medal"
            elif rank==2:
                ans[indx]="Silver Medal"
            elif rank==3:
                ans[indx]="Bronze Medal"
            else:
                ans[indx]=str(rank)
            rank+=1
        return ans

        