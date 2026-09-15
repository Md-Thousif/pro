class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in range(0,len(s)):
            if(s[i].isalnum()):
                ans+=s[i].lower()
        res=ans[::-1]
        if(res==ans):
            return True
        return False

        