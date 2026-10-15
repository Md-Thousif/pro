import heapq
class Solution(object):
    def maxProduct(self, nums):
        ans=[]
        for i in range(len(nums)):
            heapq.heappush(ans,nums[i])
            if len(ans)>2:
                heapq.heappop(ans)
        return (ans[0]-1)*(ans[1]-1)




        