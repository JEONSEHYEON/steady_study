import sys

sys.stdin = open('input.txt')

N = int(input())
count = {}
for i in range(N):
    name = sys.stdin.readline()
    try:
        count[name[0]] += 1
    except:
        count[name[0]] = 1
ans = ''
count = sorted(count.items())
for x in count:
    if x[1] >= 5:
        ans += x[0]
if ans:
    print(ans)

else:
    print('PREDAJA')
