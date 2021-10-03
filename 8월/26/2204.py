import sys

sys.stdin = open('input.txt')

while True:
    N = int(input())
    if N == 0:
        break
    words = []
    check = []
    for i in range(N):
        word = input()
        words.append(word)
        check.append([word.lower(), i])
    check.sort()
    print(words[check[0][1]])

    