class Solution:
    def reverseString(self, s: list[str]) -> None:
        i=0
        end=len(s)-1
        while(i<end):
            s[i],s[end]=s[end],s[i]
            i+=1
            end-=1
        return s


        