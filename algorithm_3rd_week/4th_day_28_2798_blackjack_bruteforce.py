import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 세가지 숫자 '모든' 조합을 골라내서 각각의 합을 구한다.
sum_list = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            new_combi = []
            new_combi.append(nums[i])
            new_combi.append(nums[j])
            new_combi.append(nums[k])
            print(new_combi)
            sum_ = sum(new_combi)
            sum_list.append(sum_)
            print(sum_list)


sum_list = list(set(sum_list))
print(sum_list)
sum_list.sort()
print(sum_list)
# 목표 점수와 차이의 합을 리스트로 모은다.
gap_list = []
for b in range(len(sum_list)):
    gap = M - sum_list[b]
    if M - sum_list[b] >= 0:
        gap_list.append(gap)
    # print(gap_list)

# 그 리스트의 길이 - 1 에 해당하는 인덱스로 gap_list의 원소를 찾으면 그것이 최대합  
# ln = len(gap_list)
print(M - gap_list[-1])
