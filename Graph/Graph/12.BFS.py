#  How to make a BFS


graph={

    'A':['B','C','D'],
    'B':['A','E','D'],
    'C':['A','D'],
    'D':['A','B','C','E'],
    'E':['B','D']
}


def DFS(queue,visited):
    if not queue:
        return 
    #visit
    last=queue.pop(0)
    print(last)
 


    #explore
    for i in graph[last]:
        if i not in visited:
            visited.add(i)
            queue.append(i)
            
    DFS(queue,visited)





visited=set('A')  
DFS(['A'],visited)         

    
    