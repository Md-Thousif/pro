class Solution:
    def isValid(self, s: str) -> bool:
        curr=[]
        for i in range(len(s)):
            if s[i] in "({[":
                curr.append(str(s[i]))
            elif len(curr)>0:
                if s[i]==")" and curr[-1]=="(":
                    curr.pop()
                elif s[i]==")" and curr[-1]!="(":
                    return False
                if s[i]=="}" and curr[-1]=="{":
                    curr.pop()
                elif s[i]=="}" and curr[-1]!="{":
                    return False
                if s[i]=="]" and curr[-1]=="[":
                    curr.pop()
                elif s[i]=="]" and curr[-1]!="[":
                    return False
            else:
                curr.append(str(s[i]))
          
        if len(curr)==0:
            return True
        else:
            return False
            

