class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        ans=[]
        nums=s1.split()+s2.split()
        m={}
        for i in range(0,len(nums)):
            if nums[i] in m:
                m[nums[i]]+=1
            else:
                m[nums[i]]=1
        for n in m:
            if(m[n]==1):
                ans.append(n)
        return ans



        