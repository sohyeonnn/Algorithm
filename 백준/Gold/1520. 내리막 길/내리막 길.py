import sys
sys.setrecursionlimit(10**9)       #재귀최대깊이설정/런타임에러해결

m, n = map(int, sys.stdin.readline().split())
height = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]   #반복계산 방지를 위해 -1로 초기화함
#dp[m-1][n-1] = 1

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    #도착 지점일시 1반환
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] == -1:  #방문하지 않았던곳은 상하좌우를 가기 전에 -1에서 0으로 바꾼다
        dp[x][y] = 0    #방문했으므로 방문표시(0)해준다

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                #상하좌우중에서 작은 값이 있는 경우 반환된 값을 현재의 dp로 저장한다
                if height[x][y] > height[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    #dfs호출된게 반환되며 dp[0][0]을 반환하게 된다
    return dp[x][y]

print(dfs(0,0))