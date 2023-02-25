import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = []

def dfs(s):
    if len(nums) == M:
        print(' '.join(map(str, nums)))
        return
    
    for i in range(s, N+1):
        if i not in nums:
            nums.append(i)
            dfs(i+1)
            nums.pop()
dfs(1)