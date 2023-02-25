import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []

def dfs():
    if len(nums) == M:
        print(' '.join(map(str, nums)))
        return
    
    for i in range(1, N+1):        
        nums.append(i)
        dfs()
        nums.pop()
        
dfs()