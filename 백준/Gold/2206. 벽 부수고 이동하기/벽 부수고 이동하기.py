#3차원 배열 사용

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())    #세로, 가로

field = []
for _ in range(n):
    field.append(list(map(int, input().rstrip())))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1    #아직 벽을 뚫은 적 없으니까 벽을 뚫을 기회가 1번 있음

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])

    while queue:
        a, b, c = queue.popleft()

        if a == n - 1 and b == m - 1:  # 우측하단(도착지점)에 도착한 경우 값을 return하고 종료한다.
            return visited[a][b][c]

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < n and 0 <= ny < m:     #범위안에 속하면서

                if field[nx][ny] == 1 and c == 0:   #벽이고 벽부술 기회를 사용하지 않은 경우
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append([nx, ny, 1])   #이번에 벽을 부순다.(c자리에 1 append = 1번 벽을 부쉇다는 의미)

                elif field[nx][ny] == 0 and visited[nx][ny][c] == 0:    #벽이 아니고 처음 와보는 곳이라면?
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append([nx, ny, c])

    else:   #도착지점에 아예 도달하지 못하는 경우에는 -1을 출력한다.
        return -1

print(bfs(0, 0, 0))