class Solution(object):
    def longestValidParentheses(self, s):
        ans=[-1]
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                ans.append(i)
            else:
                ans.pop()
                if len(ans)==0:
                    ans.append(i)
                else:
                    count=max(count,i-ans[-1])
        return count

        