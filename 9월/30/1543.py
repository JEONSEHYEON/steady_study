import sys

sys.stdin = open('input.txt')

s = input()
w = input()
i = 0
ans = 0
while True:
    if s[i] == w[0]:
        check = s[i : i + len(w)]
        if check == w:
            ans += 1
            i += len(w) - 1
    i += 1
    if i + len(w) > len(s):
        break
print(ans)
                