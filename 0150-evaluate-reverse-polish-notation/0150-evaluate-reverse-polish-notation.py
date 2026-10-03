class Solution(object):
    def evalRPN(self, t):
        ans=[]
        for i in range(len(t)):
            if t[i] == "+":
                b = int(ans.pop())
                a = int(ans.pop())
                ans.append(a + b)

            elif t[i] == "-":
                b = int(ans.pop())
                a = int(ans.pop())
                ans.append(a - b)

            elif t[i] == "*":
                b = int(ans.pop())
                a = int(ans.pop())
                ans.append(a * b)

            elif t[i] == "/":
                b = int(ans.pop())
                a = int(ans.pop())
                if a*b < 0:
                    ans.append(-(abs(a)//abs(b)))
                else:
                    ans.append(a//b)

            else:
                ans.append(int(t[i]))

        return ans[0]