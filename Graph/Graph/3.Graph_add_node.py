#adjacency matrix
def add_node(v):

    global number_of_node   #We only need to use the global keyword in a function if we want to do assignments or change the global variable. global is not needed for printing and accessing. 
    if v in nodes:
        print('node is already added')

    else:
        number_of_node=number_of_node+1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp=[]
        for i in range(number_of_node):
            temp.append(0)
        graph.append(temp)   

def display_grap():
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=' ')
        print()

nodes=[]
graph=[]
number_of_node=0

add_node('A')
add_node('B')
add_node('C')

display_grap()
print(graph)