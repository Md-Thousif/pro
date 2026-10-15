import heapq
class Solution(object):
    def numberGame(self, nums):
        ans=[]
        res=[]
        
        for i in range(len(nums)):
            heapq.heappush(ans,nums[i])
        while ans:
            alice=heapq.heappop(ans)
            bob=heapq.heappop(ans)
            res.append(bob)
            res.append(alice)
        return res

        