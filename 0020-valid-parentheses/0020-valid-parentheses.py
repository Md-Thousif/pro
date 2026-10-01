class Solution(object):
    def isValid(self, s):
        ans=[]
        if len(s)==1:
            return False
        for i in range(0,len(s)):
            if s[i] in "([{":
                ans.append(s[i])
            if len(ans)>0:
                if s[i]==")"  and ans[-1]=="(":
                    ans.pop()
                elif s[i]==")" and ans[-1]!="(":
                    return False
                if s[i]=="]" and ans[-1]=="[":
                    ans.pop()
                elif s[i]=="]" and ans[-1]!="[":
                    return False
                if s[i]=="}" and ans[-1]=="{":
                    ans.pop()
                elif s[i]=="}" and ans[-1]!="{":
                    return False
            else:
                ans.append(s[i])
        if len(ans)==0:
            return True
        return False
           


        