class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while(i<j):
            if(s[i].lower() in "aeiou" and s[j].lower() in "aeiou"):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif(s[i].lower() in "aeiou" and s[j].lower() not in "aeiou" ):
                j-=1
            elif(s[i].lower() not in "aeiou" and s[j].lower()  in "aeiou" ):
                i+=1
            else:
                i+=1
                j-=1
        return "".join(s)
            