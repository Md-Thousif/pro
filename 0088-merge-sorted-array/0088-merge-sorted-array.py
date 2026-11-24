class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        k=m+n-1
        i=m-1
        j=n-1
        
        while(i>=0 and j>=0):
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                k-=1
                i-=1
            else:
                nums1[k]=nums2[j]
                k-=1
                j-=1
        while j>=0:
            
            nums1[k]=nums2[j]
            k-=1
            j-=1
        return k
        