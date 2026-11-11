class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1=[]
        ans2=[]
        for i in range(len(s)):
            if(s[i]!='#'):
                ans1.append(s[i])
            elif s[i]=='#' and len(ans1)>0:
                ans1.pop()
        for j in range(len(t)):
            if(t[j]!='#'):
                ans2.append(t[j])
            elif t[j]=='#' and len(ans2)>0:
                ans2.pop()
        ans1=str(ans1)
        ans2=str(ans2)
        if ans1==ans2:
            return True
        return False
        


