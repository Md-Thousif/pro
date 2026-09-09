class Solution(object):
    def isHappy(self, n):
        m={}
        ans=0
        k=0
        while(n>0):
            num=n%10
            ans+=num*num
            n=n//10
            if n==0 and ans!=1:
                n=ans
                if ans not in m:
                    m[ans]=k
                    k+=1
                    ans=0
                else:
                    return False
            elif n==0 and ans==1:
                return True
        return True

            