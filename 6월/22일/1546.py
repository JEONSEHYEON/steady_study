import sys

sys.stdin = open("input.txt")

N = int(input())
grades = list(map(int , sys.stdin.readline().split()))
max_grade = max(grades)
for i in range(len(grades)):
    grades[i] = grades[i] * 100 / max_grade 


answer = sum(grades) / len(grades)
print(answer)