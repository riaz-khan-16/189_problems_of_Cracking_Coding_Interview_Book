# at firs make a graph

graph={

    'A':['B','C','D'],
    'B':['A','E','D'],
    'C':['A','D'],
    'D':['A','B','C','E'],
    'E':['B','D']
}


#make a function to traverse


visited=set()



def traverse(node,visited,graph):
    if node not in graph:
        print("is not present in the graph") 
        return 
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            traverse(i,visited,graph)

traverse('E',visited,graph)    



