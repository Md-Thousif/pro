import heapq

class Solution(object):
    def getFinalState(self, nums, k, mul):
        ans = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(ans)

        while k > 0:
            curr, idx = heapq.heappop(ans)
            nums[idx] = curr * mul
            heapq.heappush(ans, (nums[idx], idx))
            k -= 1

        return nums


        