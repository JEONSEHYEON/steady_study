새 항목
오전 9:12
임형우(모니터링매니저) 
양지웅 | simple_sort.py 
def insertion_sort():
​
    return []
​
def selection_sort():
​
    return []
​
def bubble_sort():
​
    return []
​
n = int(input())
num_list = []
​
for _ in range(n):
    num = int(input())
    num_list.append(num)
​
insertion_sorted_list = insertion_sort()
print(" ".join(map(str, insertion_sorted_list)))
​
selection_sorted_list = selection_sort()
print(" ".join(map(str, selection_sorted_list)))
​
bubble_sorted_list = bubble_sort()
print(" ".join(map(str, bubble_sorted_list)))