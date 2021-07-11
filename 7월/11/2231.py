def odd(x):
    hap = 0
    while x:
        k = x % 10
        x = x // 10
        hap += k
    return hap

import sys
sys.stdin = open("input.txt")
N = int(input())
Min = N
for i in range(N , 0 , -1):
    if i + odd(i) == N and Min > i:
        Min = i
if Min != N:
    print(Min)
else:
    print(0)
