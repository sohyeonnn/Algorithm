#커넥티드 컴포넌트 유형
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    island_days = []

    # 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                stack = [(i, j)]
                sum_ = 0
                while stack:
                    x, y = stack.pop()
                    if not visited[x][y]:
                        visited[x][y] = True
                        sum_ += int(maps[x][y])
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                                stack.append((nx, ny))
                island_days.append(sum_)

    island_days.sort()
    return island_days if island_days else [-1]