import sys

sys.stdin = open("input.txt")

N = int(input())
a = list(map(int , input().split()))
answer = []
answer.append(min(a))
answer.append(max(a))
for i in answer:
    print(i , end = ' ')