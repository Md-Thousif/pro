class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k=0
        i=0
        while(i<len(nums)):
            if nums[k]==0:
                nums.pop(k)
                nums.append(0)
            else:
                k+=1
            i+=1
        return k
        
        