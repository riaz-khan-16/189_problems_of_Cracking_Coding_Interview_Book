#  1971. Find if Path Exists in Graph

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 2

# n = 3
# edges = [[0,1],[1,2],[2,0]]
# source = 0
# destination = 2

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'is not available') 
    elif v2 not  in graph:
        print(v2, 'is not available')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

        
# at first collect all nodes

nodes=set()
for i in edges:
    for j in i:
        nodes.add(j)

#then make a graph using the nodes
        
graph={}
for i in nodes:
    graph[i]=[]

# Now add the edges

for k in edges:
    v1=k[0]
    v2=k[1]
    add_edge(v1,v2)

# well done the graph is completed
print(graph)    

# Now traverse the graph from source and if you find the destination return True


source = 0
destination = 5

visited = set()
stack = [source]
d=[]
while stack:
    node = stack.pop()
    if node not in visited:
        d.append(node)
        visited.add(node)
        for i in graph[node]:
            stack.append(i)

if destination in d:
    print(True)
          

      

