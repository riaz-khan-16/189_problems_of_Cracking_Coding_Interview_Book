tiles = "AAB"


def num_tile_possibilities(tiles):
    count = [0] * 26
    for c in tiles:
        count[ord(c) - ord('A')] += 1
    return dfs(count)

def dfs(arr):
    sum = 0
    for i in range(26):
        if arr[i] == 0:
            continue
        sum += 1
        arr[i] -= 1
        sum += dfs(arr)
        arr[i] += 1
    return sum

num_tile_possibilities(tiles)




