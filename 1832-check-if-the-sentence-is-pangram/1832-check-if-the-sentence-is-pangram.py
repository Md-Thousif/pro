class Solution:
    def checkIfPangram(self, sen: str) -> bool:
        check=97
        for i in range(26):
            if chr(check) in sen:
                check+=1
            else:
                return False
        return True