class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        m={}
        for i in range(len(nums)):
            if nums[i] in m:
                return nums[i]
            else:
                m[nums[i]]=nums[i]