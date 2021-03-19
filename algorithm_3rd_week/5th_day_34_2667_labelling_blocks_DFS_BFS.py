# import sys
# input = sys.stdin.readline
# from collections import deque

# deque 배열 설정 필요없음
# queue = deque()
# 탐색한 그곳에 1이 있다면 그 자리 좌표값을 queue에 넣어준다.
# for i in range(N):      # y 좌표
#     for j in range(N):  # x 좌표
#         if block_set[i][j] == 1:
#             queue.append([i, j])

# 토마토보다 덜 복잡. 토마토는 경로를 탐색하는 방식.
# 토마토 풀이 알고리즘은 '최단경로를 따라' 한 격자안에서
# 숫자를 증가시키는 방식. 그래서 경로를 인식시키기 위해서
# 좌표값을 queue에 넣고 빼는 작업을 넣은 것
# 여기서는 그와는 달리 1의 갯수를 세는 것이라 그럴 필요 없음.
# DFS 이용 = 종료조건 + 재귀
# data_set = 0, 1이 담긴 지도, (row, column) = 무작위 한점의 위치.
# 무작위 한점을 넣는 것이지만 (0,0)에서 DFS로 경로추적을 하는 것으로 계산하기.
def dfs_blocks(data_set, row, column):
    global houses_cnt
    # 종료조건
    if data_set[row][column] == 0:
        return 0

    # 기타 조건 + 재귀 함수 설정
    # 시작하는 위치를 0으로 바꿔 놓고 
    # 집의 갯수를 1씩 올려준다.counting).
    data_set[row][column] = 0  # 탐색한 곳은 0으로 둔다 = 또 탐색 못하게 해버림.
    # 탐색한 곳을 0으로 두기 때문에, 이 함수밖의 탐색용 for 문에서
    # 한 블록이 끝나면 만에 하나 또 그 블록으로 돌아가서 다시 탐색할 일이 생기지 않게 한다. 
    houses_cnt += 1
    # 재귀조건 설정
    for i in range(4):  # 상하좌우 4방향으로 이동하도록 설정
        new_row = row + dr[i]  # 이동한 row 위치
        new_column = column + dc[i]  # 이동한 column 위치
        # 이동한 위치가 지도 내부에 있다면 = 탐색중 밖으로 나간게 아니라면
        if 0 <= new_row < N and 0 <= new_column < N and data_set[new_row][new_column] == 1:
            # 그 좌표의 원소가 1이라면 재귀로 경로 탐색 들어간다.
            # 위의 종료조건에 따라 좌표의 원소가 0이 되는 위치에서 탐색 종료.
            dfs_blocks(data_set, new_row, new_column)

    # 토마토처럼 경로설정을 queue로 할 필요 없음.
    # while q:  # q가 빌때까지
    #     x, y = q.popleft()

# 경로측정하려는 data sest 입력
N = int(input())
block_set = []
# 단지 정보를 행(row)에 담아서 저장
for i in range(N):
    data_row = list(map(int, list(input())))
    block_set.append(data_row)

print(block_set)
# row, column 이동 방법 설정, 
dr = [0, 0, 1, -1]   
dc = [-1, 1, 0, 0]

# 탐색한다.
num_houses = []
houses_cnt = 0
for j in range(N):
    for k in range(N):
        if block_set[j][k] == 1:  # 1인 점에서 시작하라.
            houses_cnt = 0  # 집세는 값 0으로 설정하고 시작. 함수 들어가면 어차피 1로 바뀌게 된다.     
            dfs_blocks(block_set, j, k)
            num_houses.append(houses_cnt)

# 정답 출력 부분
print(len(num_houses))   # 단지의 갯수
num_houses.sort()  # 오름차순으로 출력하도록 정리
for g in num_houses:
    print(g)
