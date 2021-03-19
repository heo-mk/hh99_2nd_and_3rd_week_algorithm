import sys
input = sys.stdin.readline

N = int(input())

stairs_point = []
for i in range(N):
    stairs_point.append(int(input()))

# 기억하며 풀기의 메모장
point_accumulation_memo = []
point_accumulation_memo.append(stairs_point[0])
point_accumulation_memo.append(max(stairs_point[0] + stairs_point[1], stairs_point[1]))
point_accumulation_memo.append(max(stairs_point[0] + stairs_point[2], stairs_point[1] + stairs_point[2]))

for j in range(3, N):
    point_accumulation_memo.append(max(point_accumulation_memo[j-2] + stairs_point[j],
                                        point_accumulation_memo[j-3] + stairs_point[j-1] + stairs_point[j]))

print(point_accumulation_memo[-1])


# 개념도
# O O O O ... O     O     X    O  : dp[i] = dp[i-2] + arr[i]
# O O O O ... O     X     O    O  : dp[i] = dp[i-3] + dp[i-1] + arr[i]
# 0 1 2 3 ... i-3  i-2   i-1   i


# def stairs_accumulated_point(n, point_list):   # n = 층수, stairs = 층별 점수 모음 리스트
#     if n <= 3:
#         return stairs_point[n-1]
    
#     point_accumulation_memo = []
#     for i in range(n):
#         nth_accumulation = max(point_list[i-2] + point_list[i],
#                             point_list[i-3] + point_list[i-1] + point_list[i])
#         point_accumulation_memo.append(nth_accumulation)
#     return point_accumulation_memo[-1]