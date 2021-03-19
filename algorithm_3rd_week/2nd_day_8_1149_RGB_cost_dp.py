# 내 방식
import sys
sys.stdin = open('rgb_cost.txt', 'rt')   # 이렇게 하면 input() 부분에 txt파일의 정보가 들어간다.

# 색칠 격자표 만들기
cost_map = []
N = int(input())

# 색칠 가격 입력
for i in range(N):
    house_rgb = list(map(int, input().split()))
    cost_map.append(house_rgb)

# 값 갱신을 두번째 행부터 하니까 range(1, N)
for j in range(1, N):
    cost_map[j][0] += min(cost_map[j-1][1], cost_map[j-1][2]) 
    cost_map[j][1] += min(cost_map[j-1][0], cost_map[j-1][2])
    cost_map[j][2] += min(cost_map[j-1][0], cost_map[j-1][1])

# 마지막으로 갱신 된 값 중에서 최소값을 골라낸다.
print(min(cost_map[N-1]))


# # 금교석님 방식
# import sys
# sys.stdin = open('rgb_cost.txt', 'rt')

# # 색칠 가격 정리하기
# cost_map = []
# N = int(input())

# for i in range(N):
#     house_rgb = list(map(int, input().split()))
#     cost_map.append(house_rgb)
    
# for i in range(1 , N):
#     for j in range(N):
#         left = (j+1) % 3
#         right = (j+2) % 3
#         cost_map[i][j] += min(cost_map[i-1][left], cost_map[i-1][right])
        
# print(min(cost_map[N-1]))

