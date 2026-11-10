class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c=0
        low=0
        for i in range(len(word)):
            if word[i].isupper():
                c+=1
            else:
                low+=1
        if c==len(word) or low==len(word):
            return True
        elif word[0].isupper() and low+1==len(word):
            return True
        else:
            return False
            