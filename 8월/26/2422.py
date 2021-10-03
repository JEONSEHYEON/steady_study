import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())

ice = [[] for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    ice[x - 1].append(y - 1)

count = 0
for idx, val in enumerate(ice):
    for k in range(idx + 1, N):
        if k in val:
            continue
        x = (N - k - 1) - len(ice[k])
        if x > 0:
            count += x
print(count)
        
