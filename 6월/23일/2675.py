import sys

sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    answer = ''
    num , sentence = input().split()
    for j in sentence:
        answer += j * int(num)
    print(answer)
