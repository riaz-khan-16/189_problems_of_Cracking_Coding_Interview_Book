
graph={}
number_of_nodes=5
nodes=[1,2,3,4,5]
def add_node():
    for i in nodes:
        graph[i]=[]
    print(graph)    
add_node()
def add_edges(from_node,to_node):
    if  from_node in graph and to_node in graph:
        graph[from_node].append(to_node)

add_edges(1,2)
add_edges(2,3)
add_edges(3,4)
add_edges(4,5)
print(graph)