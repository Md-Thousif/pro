class Solution:
    def calPoints(self, ops: list[str]) -> int:
        ans=[]
        summ=0
        val=0
        for i in range(len(ops)):
            if ops[i]=='C':
                ans.pop()
            elif ops[i]=='D':
                val=ans[-1]
                ans.append(2*val)
            elif ops[i]=='+':
                a=ans.pop()
                b=ans.pop()
                ans.append(b)
                ans.append(a)
                ans.append(b+a)
            else:
                ans.append(int(ops[i]))
        for num in ans:
            summ+=num
        return summ