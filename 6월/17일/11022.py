import sys

sys.stdin = open("input.txt")

N = int(input())
answer = []
for i in range(N):
    x , y = map(int , input().split())
    answer.append([x , y])
for i in range(N):
    print(f'Case #{i + 1}: {answer[i][0]} + {answer[i][1]} = {answer[i][0] + answer[i][1]}')