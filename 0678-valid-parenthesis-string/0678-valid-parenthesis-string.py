class Solution(object):
    def checkValidString(self, s):
    
        low=0
        h=0
        for i in range(0,len(s)):
            if s[i]=="(":
                low+=1
                h+=1
            if s[i]==')':
                low -= 1
                h-= 1
            if s[i]=='*':
                low -= 1
                h += 1
            low=max(0,low)
            if h<0:
                return False
        return low==0
            