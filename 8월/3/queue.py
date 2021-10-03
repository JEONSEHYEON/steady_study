import sys

sys.stdin = open('input.txt')


N = int(input())
Queue = list(range(1 , N + 1))
front = 0
back = N - 1

for _ in range(N - 1):
    back = (back + 1) % N
    Queue[back] = Queue[front + 1]
    Queue[front] , Queue[front + 1]= None , None
    front = (front + 2) % N
    print(Queue)
    
print(Queue[back])