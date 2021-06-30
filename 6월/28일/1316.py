import sys

sys.stdin = open("input.txt")

N = int(input())
s = []
count = 0
for i in range(N):
    s.append(input())

for sentence in s:
    check = []
    for word in range(len(sentence)):
        try:
            if sentence[word] in check:
                break
            elif sentence[word] == sentence[word + 1]:
                continue
            else:
                check.append(sentence[word])
        except:
            if not sentence[word] in check:
                count += 1

print(count)

            
        


