# at firs make a graph

graph={

    'A':['B','C','D'],
    'B':['A','E','D'],
    'C':['A','D'],
    'D':['A','B','C','E'],
    'E':['B','D']
}


#make a function to traverse
start='A'
visited=set()
def dfs(graph,start,visited=None):
    if visited is None:
         visited=set()
    
    visited.add(start)
    print(start)
    for i in graph[start]:
         if i not  in visited:
              dfs(graph,i,visited)

dfs(graph,start,visited=None)               






