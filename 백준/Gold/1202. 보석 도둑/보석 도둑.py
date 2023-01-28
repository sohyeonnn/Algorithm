import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

#보석 무게 기준으로 내림차순 정렬
jewels.sort(key=lambda x:-x[0])     #x:-x[0]  --> 첫 번째 인자에 대해 역순으로(내림차순) 정렬
bags.sort(reverse = True)    #가방에 넣을 수 있는 무게 기준으로 내림차순 정렬

count = 0
heap = []

while bags:
    target = bags.pop()
    while jewels and jewels[-1][0] <= target:
        jewel = jewels.pop()
        heapq.heappush(heap, [-jewel[1], jewel[0]])

    if heap:
        count += abs(heapq.heappop(heap)[0])
print(count)