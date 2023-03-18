n = int(input()) 
k = int(input()) 
sensors = sorted(list(map(int, input().split())))

distances = [sensors[i+1] - sensors[i] for i in range(n-1)]

for i in range(k-1):
    if not distances:
        break
    max_index = distances.index(max(distances))
    distances[max_index] = 0

print(sum(distances))