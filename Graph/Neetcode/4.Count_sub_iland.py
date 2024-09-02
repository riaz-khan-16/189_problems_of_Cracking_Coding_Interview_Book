#https://leetcode.com/problems/number-of-islands/

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]



ROWS,COLS=len(grid1),len(grid2[0])
visit=set()

def dfs(r,c):
     if r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c]==0 or (r,c) in visit:
         return True
     visit.add((r,c))
     res=True
     if grid1[r][c]==0:
         res=False
     res=res and dfs(r+1,c)
     res=res and dfs(r,c+1)
     res=res and dfs(r-1,c)
     res=res and dfs(r,c-1)
     return res




count=0
for r in range(ROWS):
    for c in range(COLS):
        if grid2[r][c] and (r,c) not in visit and dfs(r,c):
            count=count+1

print(count)