# 숫자 N 입력
import sys
input = sys.stdin.readline
N = int(input())
number_set = []

# N개의 원소를 갖는 숫자 배열
for i in range(N):
    number_set.append(int(input()))
    print(number_set)

# 버블 정렬법으로 오름차순을 구현하는 함수.    
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# 정렬된 배열의 원소를 위에서부터 하나씩 출력
bubble_sort(number_set)
for k in number_set:
    print(k)        

# 선택 정렬
def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(n-i):
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]
    return array

selection_sort(number_set)
for k in number_set:
    print(k)        
