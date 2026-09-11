class Solution(object):
    def intersection(self, nums1, nums2):
        m=set(nums2)
        val=set()
        i=0
        li=[]
        while(i<len(nums1)):
            if nums1[i] in m:
                val.add(nums1[i])
                i+=1
            else:
                i+=1
        ans=list(val)
        return ans
                