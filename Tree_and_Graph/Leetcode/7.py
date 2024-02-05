points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
graph={}

def distance(v1,v2):
    return abs(v1[0]-v2[0])+abs(v1[1]-v2[1])

for i in range(len(points)):
    graph[i]=[]
print(graph)    

# graph[0].append(distance(points[0],points[1]))
# graph[0].append(distance(points[0],points[2]))
# graph[0].append(distance(points[0],points[3]))
# graph[0].append(distance(points[0],points[4]))


for x in range(len(points)):
    for i in range(len(points)):
        graph[x].append(distance(points[x],points[i]))



print(graph)

