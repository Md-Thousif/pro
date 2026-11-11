class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0,len(s),2*k):
            l=i
            r=min(i+k-1,len(s)-1)
            while(l<r):
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
