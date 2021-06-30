import sys

sys.stdin = open('input.txt')

str1 = input()
alpabet = []
for i in range(97 , 123):
    alpabet.append(chr(i))

count = [-1] * (123 - 97)

for i in str1:
    s = str1.index(i)
    c = alpabet.index(i)
    count[c] = s
for i in count:
    print(i , end = ' ')

    

      