import sys
input = sys.stdin.readline

n = int(input().rstrip())
words = []

for i in range(n):
    words.append(input().rstrip())

set_words = list(set(words))
set_words.sort()    #알파벳순
set_words.sort(key=len)     #길이순

for i in set_words:
    print(i)