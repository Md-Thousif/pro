class Solution:
    def buildArray(self, tar: list[int], n: int) -> list[str]:
        ans=[]
        k=0
        s=set(tar)
        for i in range(n):
            if i+1 in s:
                ans.append("Push")
                k+=1
                if k==len(tar):
                    return ans
            else:
                ans.append("Push")
                ans.append("Pop")

        return ans
                
