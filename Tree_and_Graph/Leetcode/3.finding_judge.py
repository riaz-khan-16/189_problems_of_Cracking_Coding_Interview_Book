n = 1 
trust = [[1,3],[2,3],[3,1]]
trust =[[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]
trust=[]
#at first collect all nodes
nodes=set()
for i in trust:
    for j in i:
       nodes.add(j)

#creat a methode to add nodes in a graph     
graph={}
for node  in nodes:
    graph[node]=[]

#make a method for adding edges
def add_edges(fr,to):
    if fr in graph and to in graph:
        graph[fr].append(to) 

#Now add the methods        
for edges in trust:
    fr=edges[0]
    to=edges[1]
    add_edges(fr,to)

#well  done the graph is done  
# now check whhich node is empty and is  available in all nodes
          
for i in nodes:
    if not graph[i]:
        count=0
        for x in graph:
            if i in graph[x]:
                count=count+1
        if count==(n-1):
            print(i)     
    









