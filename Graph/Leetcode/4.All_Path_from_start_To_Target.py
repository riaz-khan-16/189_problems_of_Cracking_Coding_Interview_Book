#797. All Paths From Source to Target

graph = [[1,2],[3],[3],[]]

def allPathsSourceTarget(graph):
    def dfs(node, path):
        if node == len(graph) - 1:
            res.append(path)
            return
        for nei in graph[node]:
            dfs(nei, path + [nei])

    res = []
    dfs(0, [0])
    return res

# Example usage:
graph = [[1, 2], [3], [3], []]
print(allPathsSourceTarget(graph))  # Output: [[0, 1, 3], [0, 2, 3]]




