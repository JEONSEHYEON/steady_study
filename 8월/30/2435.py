import sys

sys.stdin = open('input.txt')

N , K = map(int, input().split())

temp = list(map(int , input().split()))
count_max = -10000
for i in range(N - (K - 1)):
    count = 0
    for j in range(i , i + K):
        count += temp[j]
    if count > count_max:
        count_max = count

print(count_max)

