class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        ans=[]
        m={}
        num=s1.split()+s2.split()
        for i in range(len(num)):
            if(num[i] in m):
                m[num[i]]+=1
            else:
                m[num[i]]=1
        for x in m:
            if m[x]==1:
                ans.append(str(x))
        return ans    