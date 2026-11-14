class Solution:
    def twoSum(self, nums: list[int], tar: int) -> list[int]:
        m={}
        for i in range(len(nums)):
            f=nums[i]
            sec=tar-f
            if sec in m:
                return [m[sec],i]
            m[f]=i