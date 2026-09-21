class Solution(object):
    def findTheDifference(self, s, t):
        ans=0
        for ch in s:
            ans^=ord(ch)
        for ce in t:
            ans^=ord(ce)
        return chr(ans)

        