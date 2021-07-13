import sys

sys.stdin = open("input.txt")

a = list(input())
a.sort(reverse=True)
ans = ''
for s in a:
    ans += s

print(int(ans))
