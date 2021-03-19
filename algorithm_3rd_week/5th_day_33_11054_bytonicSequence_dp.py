# import sys
# input = sys.stdin.readline

# # N : 수열의 크기 ex) 10
# N = int(input()) 
# # 수열 입력 : ex) 1 5 2 1 4 3 4 5 2 1
# original_seq = list(map(int, input().split()))

# # 증가하는 수열의 원소 갯수 : memoization
# # 바이토닉 왼쪽 부분 수열 길이 재기.
# # 수열의 원소수를 memoization 하는 letf_count_set
# left_count_set = [1] * N
# for i in range(N):
#     for j in range(i):
#         if original_seq[j] < original_seq[i]:
#             left_count_set[i] = max(left_count_set[i], left_count_set[j] + 1)  # memoization
#     # print(left_count_set)

# # 바이토닉 왼쪽 부분의 수열 길이 = left_max_index
# max_val_left = max(left_count_set)
# left_max_index = left_count_set.index(max_val_left)

# # 감소하는 부분 : 바이토닉 오른쪽 수열 길이 재기
# # 감소하는 부분의 수열
# right_seq = original_seq[left_max_index+1:]

# # 바이토닉 오른쪽 수열의 memoization
# right_count_set = [1] * len(right_seq)
# for k in range(len(right_seq)):
#     for m in range(k):
#         if right_seq[m] > right_seq[k]:
#             right_count_set[k] = max(right_count_set[k], right_count_set[m]+1)
#     # print(right_count_set)

# # 바이토닉 오른쪽 부분의 수열 길이
# max_val_right = max(right_count_set)
# print(max_val_left + max_val_right)

## 지금까지 풀이는    
## 답은 맞는 경우가 있으나, 백준에서는 틀렸다고 나옴
## 그리고 중간 절차가 많아 비효율적.


## 구글링해서 찾은 방법
import sys
input = sys.stdin.readline

# N : 수열의 크기 ex) 10
N = int(input()) 
# 수열 입력 : ex) 1 5 2 1 4 3 4 5 2 1
# 원래 수열과 순서를 뒤집은 수열
original_seq = list(map(int, input().split()))
reverse_seq = original_seq[::-1]
print(original_seq)
print(reverse_seq)
print()

# 증가하는 수열의 길이를 재는 리스트
dp_increase = [1] * N
dp_decrease = [1] * N

for i in range(N):
    for j in range(i):
        if original_seq[i] > original_seq[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)
        if reverse_seq[i] > reverse_seq[j]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

print(dp_increase)
print(dp_decrease)
print()

result = [0]*N
print(result)
for k in range(N):
    result[k] = dp_increase[k] + dp_decrease[N-k-1] - 1
    
print(result)    
print(max(result))