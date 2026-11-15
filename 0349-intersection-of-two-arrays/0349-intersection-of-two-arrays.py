class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m=set(nums2)
        val=set()
        for i in range(len(nums1)):
            if nums1[i] in m:
                val.add(nums1[i])
        return list(val)