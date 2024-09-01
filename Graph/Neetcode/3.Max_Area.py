# https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows=len(grid)
        cols=len(grid[0])
        count=0
        visited=set()

        def bfs(row,col):
            area=1
            
            queue=[(row,col)]
            visited.add((row,col))
            while queue:
                x,y=queue.pop(0)
                directions=[[0,1],[1,0],[-1,0],[0,-1]]
                for i,j in directions:
                    if 0<=(x+i)<len(grid) and 0<=(y+j)<len(grid[0]):
                        if grid[x+i][y+j]==1 and (x+i,y+j) not in visited:
                            queue.append((x+i,y+j))
                            visited.add((x+i,y+j))
                            area=area+1
            return area
                
        maxarea=0    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in visited:
                    area=bfs(i,j)
                    maxarea=max(area,maxarea)
                    
        return maxarea