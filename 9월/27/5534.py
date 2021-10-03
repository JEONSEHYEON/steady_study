import sys

sys.stdin = open('input.txt')

N = int(input())

new_gan = input()

ans = 0
for i in range(N):
    old_gan = input()
    for w in range(len(old_gan)):
        if old_gan[w] == new_gan[0]:
            count = 1
            while True:
                if old_gan[w + count] == new_gan[count]:
                    count += 1
                elif count == len(new_gan):
                    ans += 1
                    break
                else:
                    break

print(ans)