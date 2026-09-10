class Solution(object):
    def firstUniqChar(self, s):
        m={}
        for i in range(0,len(s)):
            if s[i] not in m:
                m[s[i]]=1
            else:
                m[s[i]]+=1
        for j in range(0,len(s)):
            if(s[j] in m and m[s[j]]==1):
                return j
        return -1
        