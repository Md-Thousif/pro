class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans=0
        last=0
        c=0
        for i in range(k):
            if s[i] in 'aeiou':
                c+=1
        ans=c
        for j in range(k,len(s)):
            if s[j] in 'aeiou':
                c+=1
            if s[last] in 'aeiou':
                c-=1
            last+=1
            ans=max(c,ans)
        return ans