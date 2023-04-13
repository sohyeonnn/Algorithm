import sys
import heapq

n = int(sys.stdin.readline().strip())
max_heap = []
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, num)
    
    if min_heap and max_heap[0][1] > min_heap[0]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, max_value)
    
    print(max_heap[0][1])