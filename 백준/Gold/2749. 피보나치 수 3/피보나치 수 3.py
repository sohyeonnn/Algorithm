#피사노주기 이용: 피보나치 수열에서 모듈러 연산에 대한 주기가 존재, 이것이 피사노 주기
import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1
num = n % (15*100000)

for i in range(num):
    a, b = b % 1000000, (a+b) % 1000000

print(a)