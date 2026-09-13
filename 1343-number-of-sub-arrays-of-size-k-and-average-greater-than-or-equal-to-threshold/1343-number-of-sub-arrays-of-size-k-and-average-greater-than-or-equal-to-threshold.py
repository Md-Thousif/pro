class Solution(object):
    def numOfSubarrays(self, arr, k, hold):
        count=0
        summ=0
        inn=0
        for i in range(0,k):
            summ+=arr[i]
        if summ//k>=hold:
            count+=1
        for j in range(k,len(arr)):
            summ+=-arr[inn]+arr[j]
            inn+=1
            if(summ//k>=hold):
                count+=1
        return count