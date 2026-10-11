import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        ans=[]
        for num in nums:
            heapq.heappush(ans,num)
            if len(ans)>k:
                heapq.heappop(ans)
        return ans[0]