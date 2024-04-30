#backtracking means change the changes while going back

maze=[[True, True, True],
      [True, True, True],
      [True, True, True]
      ]


def f1(p,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return 
    # if not maze[r][c]:
    #     return 
   
    #down
    if r<len(maze)-1:
        f1(p+'R',maze,r+1,c)
    #right
    if  c<len(maze[0])-1:
       f1(p+'D',maze,r,c+1)
    #Up
    if r>0:
        f1(p+'R',maze,r-1,c)

    #left
    if  c>0:
       f1(p+'D',maze,r,c-1)   

     
    
f1('',maze, 0,0)
#Ans is stack overflow