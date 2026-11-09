class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans=0
        for first in s:
            ans^=ord(first)
        for end in t:
            ans^=ord(end)
        return chr(ans)

