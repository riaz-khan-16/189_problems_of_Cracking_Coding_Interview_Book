# at first make a graph

graph={

    'A':['B','C','D'],
    'B':['A','E','D'],
    'C':['A','D'],
    'D':['A','B','C','E'],
    'E':['B','D']
}


def BFS(stack, visited):
     if not stack:
          return 
     last=stack.pop()
     #visit
     print(last)
     for i in graph[last]:
          if i not in visited:
               stack.append(i)
               visited.add(i)
               BFS(stack, visited)

stack=['A']
visited=set('A')
BFS(stack, visited)

               






