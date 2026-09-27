class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        ans=[]
        nums2=s2.split()
        nums=s1.split()
        m={}
        for i in range(0,len(nums)):
            if nums[i] in m:
                m[nums[i]]+=1
            else:
                m[nums[i]]=1
        for j in range(0,len(nums2)):
            if nums2[j] in m:
                m[nums2[j]]+=1
            else:
                m[nums2[j]]=1
        for n in m:
            if(m[n]==1):
                ans.append(n)
        return ans
        

        