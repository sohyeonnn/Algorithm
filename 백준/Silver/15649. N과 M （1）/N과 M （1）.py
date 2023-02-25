import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]

per = list(permutations(nums, M))

for i in per:
    print(' '.join(map(str,i)))