import sys

sys.stdin = open("input.txt")

N = int(input())

answer = []

for i in range(N):
    val1 , val2 = map(int, input().split())
    answer.append( val1 + val2 )

for i in answer:
    print(i)