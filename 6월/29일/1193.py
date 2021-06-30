import sys

sys.stdin = open("input.txt")

N = int(input())
i = 0
hap = 0
while True:
    i += 1
    hap += i
    if hap >= N:
        break
if i % 2 != 0:
    a = 1 + (hap - N)
    b = i - (hap - N)
else:
    a = i - (hap - N)
    b = 1 + (hap - N)

print(f'{a}/{b}')