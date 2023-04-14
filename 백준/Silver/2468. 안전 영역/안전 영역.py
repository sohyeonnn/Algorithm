import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

max_height = max(map(max, graph))
max_safe_area = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, rain, n, visited, graph):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if not visited[x][y] and graph[x][y] > rain:
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, rain, n, visited, graph)

        return True
    return False

for rain in range(max_height):
    visited = [[False] * n for _ in range(n)]
    safe_area = 0
    
    for i in range(n):
        for j in range(n):
            if dfs(i, j, rain, n, visited, graph):
                safe_area += 1

    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)