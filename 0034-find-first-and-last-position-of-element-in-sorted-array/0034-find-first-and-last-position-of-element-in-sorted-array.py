class Solution:
    def searchRange(self, nums: list[int], tar: int) -> list[int]:
        
        def first():
            fir=-1
            i=0
            j=len(nums)-1
            while(i<=j):
                mid=i+(j-i)//2
                if(nums[mid]==tar):
                    fir=mid
                    j=mid-1
                elif(nums[mid]<tar):
                    i=mid+1
                else:
                    j=mid-1
            return fir
        def last():
            las=-1
            i=0
            j=len(nums)-1
            while(i<=j):
                mid=i+(j-i)//2
                if(nums[mid]==tar):
                    las=mid
                    i=mid+1
                elif(nums[mid]<tar):
                    i=mid+1
                else:
                    j=mid-1
            return las
        return [first(),last()]