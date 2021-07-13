import sys

sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
ans = [0] * 10000
for i in range(N):
    ans[int(sys.stdin.readline()) - 1] += 1
for i in range(len(ans)):
    for j in range(ans[i]):
        print(i + 1)