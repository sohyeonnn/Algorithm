import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []

def dfs(cnt, k):
    if cnt-1 == M:
        print(' '.join(map(str, nums)))
        return
    
    for i in range(k, N+1):
        nums.append(i)
        dfs(cnt+1, i)
        nums.pop()
        
dfs(1, 1)