# 백준 1920번 문제
import sys
input = sys.stdin.readline

# N개의 정수로 된 수열 생성
N = int(input())
seq1 = list(map(int, input().split()))

# M개의 정수로 된 수열 생성
# 이 수열에 있는 숫자가 
# 먼저 만든 수열 안에 있는지 확인한다.
M = int(input())
seq2 = list(map(int, input().split()))

# 이분 탐색을 위한 정렬
seq1.sort()
print(seq1)
print(seq2)

# M개 정수로 된 수열안의 숫자들이
# N개 정수로 된 수열안에 있는지 확인하기
def binary_check(arr: list, num: int):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if num == arr[mid]:
            return 1
        elif num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0  # 답을 찾지 못하면 -1 반환 

# seq2에 있는 모든 원소를 대상으로 이분탐색
for j in range(M): 
    print(binary_check(seq1, seq2[j]))