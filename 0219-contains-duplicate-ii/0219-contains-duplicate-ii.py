class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        s=set()
        c=0
        l=0
        for i in range(0,len(nums)):
            if c>k:
                c-=1
                s.remove(nums[l])
                l+=1
            if nums[i] in s:
                if c<=k:
                    return True
            else:
                s.add(nums[i])
                c+=1
        return False
            
        