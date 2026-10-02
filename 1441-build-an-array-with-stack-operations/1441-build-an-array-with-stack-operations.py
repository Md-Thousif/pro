class Solution(object):
    def buildArray(self, tar, n):
        i=0
        j=1
        ans=[]
        while(i<len(tar)):
            if tar[i]==j:
                ans.append("Push")
                i+=1
            else:
                ans.append("Push")
                ans.append("Pop")
            j+=1
        return ans
