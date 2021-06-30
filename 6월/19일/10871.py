import sys

sys.stdin = open("input.txt")
N , M = map(int , input().split())

a = list(map(int , input().split()))
answer = []
for i in a:
    if i < M:
        answer.append(i)

for i in answer:
    print(i , end = ' ')
