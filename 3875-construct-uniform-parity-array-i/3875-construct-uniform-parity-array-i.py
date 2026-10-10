class Solution(object):
    def uniformArray(self, nums1):
        nums2=[]
        for i in range(0,len(nums1)):
            if nums1[i]%2==1:
                nums2.append(nums1[i])
                
        for j in range(len(nums1)):
            if len(nums2)>0:
                if nums1[j]%2==0:
                    nums2.append(nums2[0]-nums1[j])
        return True



        