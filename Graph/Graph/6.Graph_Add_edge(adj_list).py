graph={}

def add_node(v):
    if v in graph:
        print(v,'node is already available')
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'is not available') 
    elif v2 not  in graph:
        print(v2, 'is not available')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


print('before adding',graph)    
add_node('A') 
add_node('B') 
add_node('C') 
add_node('D')  
add_node('E')  

add_edge('A','B')
add_edge('A','C')
add_edge('A','D')
add_edge('A','E')
add_edge('B','D')
print(graph) 



