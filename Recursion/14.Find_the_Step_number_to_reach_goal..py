#backtracking means change the changes while going back

maze=[[True, True, True],
      [True, True, True],
      [True, True, True]
      ]


def f1(p,maze,r,c,path,step):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return 
    if not maze[r][c]:
        return
    #make a change
    maze[r][c]=False
   
    #down
    if r<len(maze)-1:
        f1(p+'R',maze,r+1,c,path,step+1)
    #right
    if  c<len(maze[0])-1:
       f1(p+'D',maze,r,c+1,path,step+1)
    #Up
    if r>0:
        f1(p+'R',maze,r-1,c,path,step+1)

    #left
    if  c>0:
       f1(p+'D',maze,r,c-1,path,step+1)  

    #revert the change
    maze[r][c]=True    

     
    
f1('',maze, 0,0)
#Ans is stack overflow