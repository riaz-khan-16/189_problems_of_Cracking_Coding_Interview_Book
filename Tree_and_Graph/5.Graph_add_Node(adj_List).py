graph={}

def add_node(v):
    if v in graph:
        print(v,'node is already available')
    else:
        graph[v]=[]

print('before adding',graph)    
add_node('A') 
add_node('B') 
add_node('C') 
add_node('D')  
add_node('E')      
print(graph) 



