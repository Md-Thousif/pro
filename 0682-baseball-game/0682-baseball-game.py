class Solution(object):
    def calPoints(self, ope):
        ans=[]
        for i in range(0,len(ope)):
            if(ope[i]=='+' and len(ans)>1):
                ans.append(int(ans[len(ans)-1])+int(ans[len(ans)-2]))
            elif ope[i]=='D' and len(ans)>0:
                ans.append(2*int(ans[len(ans)-1]))
            elif ope[i]=='C' and len(ans)>0:
                ans.pop()
            elif ope[i] !='+' and ope[i]!='D' and ope[i]!='C':
                ans.append(ope[i])
        summ=0
        for j in range(0,len(ans)):
            summ+=int(ans[j])
        return summ
        