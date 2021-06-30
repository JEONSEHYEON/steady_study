import sys

sys.stdin = open("input.txt")

N = int(input())
hap = 0
for i  in range(N + 1):
    hap += i

print(hap)