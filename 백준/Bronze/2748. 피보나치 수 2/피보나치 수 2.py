import sys
input = sys.stdin.readline

n = int(input())

arr = [i for i in range(n+1)]
arr[1] = 1

for i in range(2, n+1) :
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr[-1])