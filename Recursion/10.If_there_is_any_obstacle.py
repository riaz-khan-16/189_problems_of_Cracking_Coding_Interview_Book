#backtracking means change the changes while going back

maze=[[True, True, True],
      [True, False, True],
      [True, True, True]]


def f1(p,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return 
    if not maze[r][c]:
        return 
   
    if r<len(maze)-1:
        f1(p+'R',maze,r+1,c)
    if  c<len(maze[0])-1:
       f1(p+'D',maze,r,c+1)
     
    
f1('',maze, 0,0)