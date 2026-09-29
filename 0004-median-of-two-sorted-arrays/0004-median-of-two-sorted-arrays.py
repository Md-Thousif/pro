class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i=0
        j=0
        res=[]
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<nums2[j]):
                res.append(nums1[i]) 
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        if(len(res)%2==1):
            ans=len(res)//2
            return res[ans]
        else:
            ans1=len(res)//2
            fin=res[ans1-1]+res[ans1]
            return fin/2.0


        