import heapq
class Solution(object):
   
    def topKFrequent(self, nums, k):
        m={}
        ans=[]
        for i in range(0,len(nums)):
            if nums[i] not in m:
                m[nums[i]]=1
            else:
                m[nums[i]]+=1
        for num,fer in m.items():
            heapq.heappush(ans,(fer,num))
            if len(ans)>k:
                heapq.heappop(ans)
        return [num for freq, num in ans]   
        # this two returns doing the same thing you can write like this also    
        '''res=[]
        for num,freq in ans:
            res.append(numm)'''
        
        
        