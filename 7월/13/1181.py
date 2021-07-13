import sys

sys.stdin = open("input.txt")

N = int(input())
a = {}
for i in range(N):
    s = input()
    len_s = len(s)
    if len_s in a:
        if s in a[len_s]:
            continue
        a[len_s].append(s)
    else:
        a[len_s] = [s]
a = sorted(a.items())
for i in a:
    i[1].sort()

for i in a:
    for j in i[1]:
        print(j)