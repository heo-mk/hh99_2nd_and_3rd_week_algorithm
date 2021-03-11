# N = int(input())     # N = 수열의 크기

# # N 길이를 갖는 수열(set type) 생성
# sequence = list(map(int, input().split()))
# print(sequence)
# # 공통 원소 하나만 남김 : set
# sequence_set = set(sequence)
# set_length = len(sequence_set)
# print(sequence_set)
# print(set_length)

# # 수열 내부의 공통 원소 하나만 갖는 set들 생성 : set 이용
# sequence_dict = {1:[]}
# for i in range(set_length):
#     sequence_dict[j] = sequence_set.pop()

# print(sequence_dict)

################################################################
############### set type 변환으로 접근하기 실패 ################
################################################################
################################################################
################ list 끼리 비교하기 식으로 변환 ################


N = int(input())     # N = 수열의 크기
sequence = list(map(int, input().split()))  # N개만큼 넣어준다.

# dynamic programming의 memorization 용 리스트 생성
count_set = [1] * N     # memorization, 이걸 출력용으로 쓴다.
# count_set = [0] * N     # if 문이 다른 버전일 경우.
# sequence list와 count_list는 1대 1 대응. index도 1대 1 대응.
# 그런데 count_list의 원소들은 sequence list의 같은 index 원소와 비교하면서 증가하면 1씩 올린다.
# sequence list의 가장 작은 값을 기준으로 시작한다.

for i in range(N):
    for j in range(i):
        # if sequence[j] < sequence[i]:
        #     count_set[i] = max(count_set[i], count_set[j]+1)
            
        if sequence[j] < sequence[i] and count_set[j] > count_set[i]:
            count_set[i] = count_set[j]
        count_set[i] += 1  # dynamic programming에서 저장 시행 하는 부분.       
    print(count_set)
    
print(count_set)
print(max(count_set))
    