class Solution:
    def isHappy(self, n: int) -> bool:
        m={}
        k=0
        ans=0
        while(n>0):
            f=n%10
            ans+=f*f
            n=n//10
            if n==0 and ans==1:
                return True
            elif n==0 and ans!=1:
                n=ans
                if ans in m:
                    return False
                else:
                    m[ans]=k
                    k+=1
                    ans=0
