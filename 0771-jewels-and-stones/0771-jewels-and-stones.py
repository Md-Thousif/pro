class Solution:
    def numJewelsInStones(self, jew: str, sto: str) -> int:
        c=0
        for i in range(len(sto)):
            if sto[i]  in jew:
               c+=1
      
        return c