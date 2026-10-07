class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n=1
        m={}
        ans=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] not in m:
                    m[grid[i][j]]=1
                else:
                    ans.append(grid[i][j])
        for x in m:
            if(n not in m):
                ans.append(n)
            n+=1
        if len(ans)==1:
            ans.append(n)
        return ans


                
        