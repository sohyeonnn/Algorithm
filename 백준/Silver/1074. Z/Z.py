import sys

n, r, c = map(int, sys.stdin.readline().split())

res = 0

while n > 1:
    ran = 2 ** (n-1)    #4등분 중 몇번째 위치인지
    if r >= ran:
        if c >= ran:
            res += (4 ** (n-1)) * 3
            r -= ran
            c -= ran
        else:
            res += (4 ** (n - 1)) * 2
            r -= ran

    else:
        if c >= ran:
            res += (4 ** (n - 1)) * 1
            c -= ran
        else:
            pass
    n -= 1

if r == 0:
    if c == 0:
        print(res)
    else:
        print(res + 1)
else:
    if c == 0:
        print(res + 2)
    else:
        print(res + 3)