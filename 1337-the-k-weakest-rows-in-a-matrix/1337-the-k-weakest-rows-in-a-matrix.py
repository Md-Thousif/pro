import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        ans=[]
        res=[]
        
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
            heapq.heappush(ans,(-count,-i))
            if len(ans)>k:
                heapq.heappop(ans)
        ans.sort(reverse=True)
        for num,idx in ans:
            res.append(-idx)
       
        return res
        