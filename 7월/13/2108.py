import sys

sys.stdin = open("input.txt")

N = int(input())
ans = [0] * 8001
count = 0
sor = []
bin = []
for i in range(N):
    k = int(input())
    if k < 0:
        ans[abs(k) - 1] += 1
    else:
        ans[k + 4000] += 1
for i in range(len(ans)):
    for j in range(ans[i]):
        if i < 4000:
            k = 0 - i
            sor.append(k -1)
        else:
            sor.append(i - 4000)
sor.sort()
print(round(sum(sor) / N))
print(sor[N // 2])
da = max(ans)

for i in range(len(ans)):
    if da == ans[i]:
        if i < 4000:
            k = 0 - i 
            bin.append(k -1)
        else:
            bin.append(i - 4000)

bin.sort()
if len(bin) > 1:
    print(bin[1])
else:
    print(bin[0])
print(sor)
print(sor[-1] - sor[0])
