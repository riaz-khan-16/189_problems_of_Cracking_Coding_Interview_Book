


# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
#route between two nodes.

# at first make a graph


#    

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': []
}

graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['E'],
    'E': ['A']
}

start='A'
visited=set()
def dfs(graph,start,end,visited=None):
    if visited is None:
         visited=set()
    print(start==end)
    visited.add(start)
    for i in graph[start]:
         if i not  in visited:
              dfs(graph,i,end,visited)

dfs(graph,start,'E',visited=None)               
