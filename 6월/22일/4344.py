import sys

sys.stdin = open("input.txt")

classes = int(input())
data = []
answer = []
for i in range(classes):
    data.append(list(map(int , input().split())))

for data_list in data:
    count = 0
    avr = (sum(data_list) - data_list[0]) / data_list[0]
    for i in range(1 , len(data_list)):
        if  data_list[i] > avr:
            count += 1
    print('{:.3f}%'.format(count * 100 / data_list[0]))

    




