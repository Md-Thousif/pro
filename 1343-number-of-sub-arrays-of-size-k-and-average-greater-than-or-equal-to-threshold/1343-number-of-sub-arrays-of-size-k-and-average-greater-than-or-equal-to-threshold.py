class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, thres: int) -> int:
        summ=0
        inx=0
        c=0
        for i in range(k):
            summ+=arr[i]
        if summ/k>=thres:
            c+=1
        for j in range(k,len(arr)):
            summ=(summ-arr[inx]+arr[j])
            inx+=1
            if summ/k>=thres:
                c+=1
        return c
