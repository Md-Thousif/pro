class Solution(object):
    def checkIfExist(self, arr):
        m={}
        for i in range(0,len(arr)):
            m[arr[i]]=i
        for j in range(0,len(arr)):
            tar=2*arr[j]
            if(tar in m and m[tar]!=j):
                return True
        return False
        