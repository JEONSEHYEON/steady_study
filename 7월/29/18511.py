import sys

sys.stdin = open('input.txt')

N , M = map(int , input().split())
oneso = list(map(str , input().split()))

oneso.sort()
oneso.reverse()
N = list(str(N))
def dfs(i):
    ans = ''
    if i == len(N):
        return
    for s in oneso:
        if N[i] == s:
            ans += s
            dfs(i + 1)
            break
        elif N[i] > s:
            ans += s
            for k in range(len(N) - 1):
                ans += oneso[0]
            break
    if not ans:
        for k in range(len(N) - 1):
            ans += oneso[0]
    return int(ans)

print(dfs(0))
            



# for i in range(N , -1 , -1):
#     ans = list(str(i))
#     count = 0
#     for j in ans:
#         if j in oneso:
#             count += 1
#         else:
#             break
#     if count == len(ans):
#         print(i)
#         break
