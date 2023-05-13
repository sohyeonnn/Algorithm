import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

list = []
for i in range(n):
    list.append(i+1)

for j in permutations(list, n):
    for k in range(n):
        print(j[k], end=" ")
    print()