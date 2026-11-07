class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]]+=1
            else:
                m[s[i]]=1
        for j in range(len(t)):
            if t[j] in m:
                m[t[j]]-=1
            else:
                return False
        for x in m:
            if m[x]!=0:
                return False
        return True
