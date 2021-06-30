import sys

sys.stdin = open("input.txt")

a = list(input() for _ in range(2))
a[0] = int(a[0])
a[1] = int(a[1])

if a[0] < 0 and a[1] < 0:
    print(3)
if a[0] > 0 and a[1] < 0:
    print(4)
if a[0] < 0 and a[1] > 0:
    print(2)
if a[0] > 0 and a[1] > 0:
    print(1)