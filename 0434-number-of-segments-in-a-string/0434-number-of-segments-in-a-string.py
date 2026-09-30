class Solution(object):
    def countSegments(self, s):
        c=0
        i=0
        while(i<len(s)):
            if(s[i]!=' '):
                if(i==0 or s[i-1]==' '):
                    c+=1
            i+=1
        return c
            