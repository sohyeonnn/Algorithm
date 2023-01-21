import sys
input = sys.stdin.readline

n = int(input())
coding_level = list(map(int, input().split()))
coding_level.sort()

team = []

for i in range(len(coding_level)):
    team.append(coding_level[i] + coding_level[len(coding_level)-1-i])
print(min(team))