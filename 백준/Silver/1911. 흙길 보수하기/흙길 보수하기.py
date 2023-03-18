n, l = map(int, input().split())
holes = []

for i in range(n):
    x, y = map(int, input().split())
    holes.append((x, y))

holes.sort()
count = 0
start = 0
for hole in holes:
    if start >= hole[1]:
        continue
    else:
        if start < hole[0]:
            start = hole[0]
        count += (hole[1] - start + l - 1) // l
        start += (hole[1] - start + l - 1) // l * l

print(count)