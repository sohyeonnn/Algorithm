import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)  # 컴퓨터 번호의 인덱스에 연결된 컴퓨터 번호를 리스트로 저장

result = []
max_value = -1

def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)  # 이미 이전에 방문한 노드인지 확인
    visited[start] = True
    count = 1

    while queue:
        v = queue.popleft()  # 큐의 앞에서부터 노드를 꺼내서
        for e in graph[v]:  # 해당 노드와 연결된 노드를 순서대로 확인
            if not visited[e]:  # 연결된 노드를 아직 방문하지 않은 경우
                queue.append(e)  # 큐에 추가 후
                visited[e] = True  # 방문한 것으로 처리
                count += 1  # 방문한 노드 수 + 1

    return count  # 주어진 노드와 연결된 노드 개수 반환


for i in range(1, n+1):  # 모든 컴퓨터 번호 확인
    c = bfs(i)  # 연결된 컴퓨터 수 확인
    if c > max_value:  # 현재 연결된 컴퓨터 수가 기존 최대 연결 컴퓨터 수보다 큰 경우
        max_value = c  # 현재 연결된 컴퓨터 수로 최대값 수정
        result = [i]  # 해당 컴퓨터 번호도 수정
    elif c == max_value:  # 현재 연결된 컴퓨터 수가 기존 최대 연결 컴퓨터 수와 같은 경우
        result.append(i)  # 해당 컴퓨터 번호 추가

for r in result:
    print(r, end=" ")