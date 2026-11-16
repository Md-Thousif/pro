class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m={}
        ans=[]
        n=1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in m:
                    ans.append(grid[i][j])
                else:
                    m[grid[i][j]]=1
        for k in m:
            if n not in m:
                ans.append(n)
            n+=1
        if len(ans)==1:
            ans.append(n)
        return ans  
