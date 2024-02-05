# at first make a graph

nodes=[]
graph=[]

#there  are two ways to implement any graph
# 1. Adjacency Matrix
# 2. Adjacency List

count_of_nodes=0

#I will make to insert any element in the graph

def insert_node(new_node):
    global count_of_nodes
    #at first it will check if the node is already available in the graph or not
    if new_node in nodes:
        #show that it is already available
        print('The node is already available')

    else:
        count_of_nodes=count_of_nodes+1

        nodes.append(new_node)
        # we need to increase a row
        temp=[]
        for  i in range(count_of_nodes):
            temp.append(0)
    
        for i in graph:
            i.append(0)
        graph.append(temp)    

def add_edge(v1,v2):
             #check at first they are available or not
    
        if v1 not in nodes:
             print(v1,'Not available')
        elif v2 not in nodes:
              print(v2,'Not available')
        else:
             #at first find their index
             index1=nodes.index(v1)    
             index2=nodes.index(v2)   
             graph[index1][index2]=1
             graph[index2][index1]=1

def delete_edge(node):
     global count_of_nodes
     #check it is available in the graph or not
     if node not in nodes:
          print(node, 'is not in the graph')
     else:
          #at first find the index
          ind=nodes.index(node)
          #then remove from node list
          nodes.pop(ind)
          #then remove row fraph
          graph.pop(ind)
          #then decrease count of nodes
          count_of_nodes=count_of_nodes-1
          #then remove the column
          for i in graph:
               i.pop(ind)



             
  

insert_node('A')

insert_node('B')
insert_node('C')
insert_node('D')
add_edge('A','B')
add_edge('B','D')
add_edge('C','D')
add_edge('A','C')
delete_edge('D')
delete_edge('A')
delete_edge('B')

print(graph)            
        
        





