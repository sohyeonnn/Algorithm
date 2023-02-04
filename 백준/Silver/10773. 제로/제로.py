import sys
input = sys.stdin.readline

k = int(input().rstrip())

stack = []
for i in range(k):
    number = int(input().rstrip())
    #print(stack)

    if number == 0:
        stack.pop()     #제일 마지막에 들어갔던 0이 아닌 수가 pop 된다
    else:
        stack.append(number)

print(sum(stack))