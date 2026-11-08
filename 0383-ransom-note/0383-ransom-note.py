class Solution:
    def canConstruct(self, ran: str, mag: str) -> bool:
        m={}
        count=0
        for i in range(len(mag)):
            if mag[i] in m:
                m[mag[i]]+=1
            else:
                m[mag[i]]=1
        for j in range(len(ran)):
            if ran[j] in m and m[ran[j]]!=0:
                m[ran[j]]-=1
                count+=1
            else:
                return False
        if count==len(ran):
            return True
        else:
            return False
        
