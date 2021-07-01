import sys

sys.stdin = open("input.txt")

N = int(input())
count = 0
for i in range(N // 5 , -1 , -1):
    if not (N - i * 5) % 3:
        count += (N - i * 5) // 3 + i
        print(count)
        break
    elif i == 0:
        print(-1)