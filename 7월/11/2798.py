import sys

sys.stdin = open("input.txt")

N , M = map(int , input().split())
a = list(map(int , input().split()))
len_a = len(a)
max = 0
for i in range(len_a - 2):
    for j in range(i + 1 , len_a - 1):
        for k in range(j + 1 , len_a):
            hap = a[i] + a[j] + a[k]
            if hap <= M and max < hap:
                max = hap

print(max)

