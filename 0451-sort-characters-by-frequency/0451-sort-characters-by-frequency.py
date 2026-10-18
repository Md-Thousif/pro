import heapq
class Solution(object):
    def frequencySort(self, s):
        ans=[]
        m={}
        res=''
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=1
            else:
                m[s[i]]+=1
        for key,val in m.items():
            heapq.heappush(ans,(-val,key))
        while ans:
            v,k=heapq.heappop(ans)
            while v!=0:
                res+=k
                v+=1
        return res

    

        