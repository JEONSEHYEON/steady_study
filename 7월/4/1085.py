import sys

sys.stdin = open("input.txt")

a = list(map(int , input().split()))

print(min(abs(a[0] - a[2]) , abs(a[1] - a[3]) , abs(a[0]) , abs(a[1])))