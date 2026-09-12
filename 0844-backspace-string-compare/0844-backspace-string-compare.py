class Solution(object):
    def backspaceCompare(self, s, t):
        ans1=[]
        ans2=[]
        for i in range(0,len(s)):
            if s[i]=='#':
                if len(ans1)>0:
                    ans1.pop()
            else:
                ans1.append(s[i])
        res1="".join(ans1)
        for j in range(0,len(t)):
            if t[j]=='#':
                if len(ans2)>0:
                    ans2.pop()
            else:
                ans2.append(t[j])
        res2="".join(ans2)
        if res1==res2:
            return True
        return False