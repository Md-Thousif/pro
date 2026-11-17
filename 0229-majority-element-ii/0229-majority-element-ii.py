class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        m={}

        ans=set()
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]]+=1
            else:
                m[nums[i]]=1
            if m[nums[i]]>len(nums)/3:
                ans.add(nums[i])
        return list(ans)