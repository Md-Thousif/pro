class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        m={'(','{','['}
        for i in range (len(s)):
            if s[i] in m:
                ans.append(str(s[i]))
            if len(ans)>0:
                if s[i]==')' and ans[-1]=='(':
                    ans.pop()
                elif s[i]==')' and ans[-1]!='(':
                    ans.append(str(s[i]))
                if s[i]=='}' and ans[-1]=='{':
                    ans.pop()
                elif s[i]=='}' and ans[-1]!='{':
                    ans.append(str(s[i]))
                if s[i]==']' and ans[-1]=='[':
                    ans.pop()
                elif s[i]==']' and ans[-1]!='[':
                    ans.append(str(s[i]))
                
            else:
                ans.append(str(s[i]))
        if len(ans)==0:
            return True
        return False
            


