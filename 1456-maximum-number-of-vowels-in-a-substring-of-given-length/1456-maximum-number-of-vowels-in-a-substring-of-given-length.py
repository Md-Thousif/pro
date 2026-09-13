class Solution(object):
    def maxVowels(self, s, k):
        m={'a','e','i','o','u'}
        curr=0
        inn=0
        for i in range(0,k):
            if s[i] in m:
                curr+=1
        maxx=curr
        for j in range(k,len(s)):
            if(s[j] in m): 
                curr+=1
            if s[inn] in m:
                curr-=1
            inn+=1
            maxx=max(curr,maxx)
        return maxx