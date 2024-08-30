# 1791. Find Center of Star Graph

edges =  [[1,2],[2,3],[4,2]]



#collect all nodes

def collect_all_nodes(edges):
    nodes=set()
    for i in edges:
        for j in i:
           nodes.add(j)
    return nodes   
all_nodes=collect_all_nodes(edges)
graph={}    

def add_nodes():
    for i in all_nodes:
        graph[i]=[]
    print(graph)


def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,'is not available') 
    elif v2 not  in graph:
        print(v2, 'is not available')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)



def  add_edges():
    for i in edges:
        v1=i[0]
        v2=i[1]   
        add_edge(v1,v2)

        

add_nodes() 
add_edges()
print(graph) 

for i in graph:
    if len(graph[i])==len(all_nodes)-1:
        print(i)


         

#       





    