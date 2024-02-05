rooms =[[1,3],[1,4],[2,3,4,1],[],[4,3,2]]


def canVisitAllRooms(rooms):

        n=len(rooms)   
        #make a graph
        graph={}
        for i in range(n):
            graph[i]=rooms[i]

        #now traverse the graph and count room
        visited=set()
        
        def dfs(graph,start,visited):

            visited.add(start)
            for i in graph[start]:
                if i not  in visited:
                    dfs(graph,i,visited)
        
        dfs(graph,0,visited)
        if len(visited)==n:
            return True
        else:
            return False  
        
        