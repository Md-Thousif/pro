class Solution:
    def wordPattern(self, patt: str, s: str) -> bool:
        s=s.split()
        if(len(s)!=len(patt)):
            return False
        m={}
        k={}
        for i in range(len(patt)):
            if patt[i] in m and m[patt[i]]!=s[i]:
                return False
            if s[i] in k and k[s[i]]!=patt[i]:
                return False
            m[patt[i]]=s[i]
            k[s[i]]=patt[i]
        return True