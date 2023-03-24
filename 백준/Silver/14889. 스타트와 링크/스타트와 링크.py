n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_diff = 1e9  # 최소 시너지 차이를 저장하는 변수

def dfs(depth, start):
    global min_diff
    
    if depth == n // 2:  # 팀을 다 나누었을 경우
        start_team = []
        link_team = []
        for i in range(n):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)
        
        # 팀 시너지 계산
        start_synergy = 0
        link_synergy = 0
        for i in range(n // 2):
            for j in range(i+1, n // 2):
                start_synergy += synergy[start_team[i]][start_team[j]] + synergy[start_team[j]][start_team[i]]
                link_synergy += synergy[link_team[i]][link_team[j]] + synergy[link_team[j]][link_team[i]]
        
        # 최소 시너지 차이 갱신
        min_diff = min(min_diff, abs(start_synergy - link_synergy))
        return
    
    # 팀 나누기
    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(min_diff)