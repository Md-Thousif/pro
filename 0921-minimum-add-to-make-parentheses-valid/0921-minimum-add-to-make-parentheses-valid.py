class Solution(object):
    def minAddToMakeValid(self, s):
        openn=0
        ans=0
        for i in range(0,len(s)):
            if s[i]=="(":
                openn+=1
            else:
                if openn>0:
                    openn-=1
                else:
                    ans+=1
        return openn+ans
        