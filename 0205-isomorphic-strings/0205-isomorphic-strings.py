class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m={}
        k={}
        for i in range(len(s)):
            if s[i] in m and m[s[i]]!=t[i]:
                return False
            if t[i] in k and k[t[i]]!=s[i]:
                return False
            m[s[i]]=t[i]
            k[t[i]]=s[i]
        return True