class Solution:
    def numJewelsInStones(self, jew: str, sto: str) -> int:
        m={}
        c=0
        for i in range(len(jew)):
            if jew[i] not in m:
                m[jew[i]]=1
        for j in range(len(sto)):
            if sto[j] in m:
                c+=1
        return c