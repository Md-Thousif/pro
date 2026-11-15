class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans=[]
        m=set(nums)
        for i in range(1,len(nums)+1):
            if i not in m:
                ans.append(i)
        return ans