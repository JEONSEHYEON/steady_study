import sys

sys.stdin = open('input.txt')


N , M = map(int , input().split())

dnas = [[] for _ in range(M)]
ans = ''
dist = 0

for _ in range(N):
    dna = list(input())
    for i in range(M):
        dnas[i].append(dna[i])

for i in range(M):
    acgt = {'A':0 , 'C':0 , 'G':0, 'T':0}
    for s in dnas[i]:
        acgt[s] += 1
    acgt_sort = sorted(acgt.items(),reverse=True, key = lambda item: item[1])
    ans += acgt_sort[0][0]
    dist += (N - acgt_sort[0][1])


print(ans, dist)

        