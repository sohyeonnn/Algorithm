import sys

n = int(sys.stdin.readline().rstrip())

time = []
cost = []
dp = []

for i in range(n):
    Ti, Pi = map(int, sys.stdin.readline().split())
    time.append(Ti)
    cost.append(Pi)
    dp.append(Pi)
dp.append(0)    #error방지; index list out of range

for i in range(n-1, -1, -1):    #뒤에서부터 확인
    if time[i] + i > n:     #데드라인이 기한을 넘어가는 경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], cost[i] + dp[i + time[i]])
print(dp[0])