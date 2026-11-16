class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        m={}
        for i in range(len(arr)):
            m[arr[i]]=i
        for j in range(len(arr)):
            val=2*arr[j]
            if val in m and m[val]!=j:
                return True
        return False
            