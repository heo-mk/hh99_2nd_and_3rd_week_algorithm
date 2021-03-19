# BFS를 해야 하는 이유는 
# 현재 위치에서 상하좌우로 모두 이동하며 익히는 절차니까
# 한놈만 아니 한 방향만 패면서 나아가는 절차가 아니다.
# 이동하면서 새로 익혀버리는 위치 정보를 queue에 저장하고, 
# 다음번 이동하면서 다음 것을 익힐 때 바로 이전에 저장된걸 빼버린다.
# 이것이 바로 queue

# BFS이므로 queue. deque 모듈로 시간을 줄인다.
import sys
from collections import deque
input = sys.stdin.readline

# x,y 이동 법칙 설정. 행렬에서 x,y 좌표가 정해진 규칙에 따른다.
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


# 여기서부터는 토마토 격자, 격자의 칸마다 있는 토마토의 성질(익음, 안 익음, 없음) 설정해준다.
# 토마토 격자 너비, 폭 설정
w, h = map(int, input().split())
matrix = [list(map(int, input().split())) for m in range(h)]  # 격자안에 1,0,-1 등으로 토마토 상태 설정
print(matrix)

# x,y 이동 법칙 설정. 행렬에서 x,y 좌표가 정해진 규칙에 따른다.
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# queue 배열 설정. 
queue = deque()

# 이미 익은 과일 자리라면(1이 있다면) 
# 그 자리 좌표값을 queue에 넣어준다. 
# 넣어주는 것은 그 자리에 있는 숫자가 아니다!
# 좌표값이다!
for i in range(h):
    for j in range(w):
        if matrix[i][j] == 1:
            queue.append([i, j])

# 하루당 익는 토마토 전파 속도를 설정하는 함수 : BFS
def bfs_tomato(q): # q = queue
    while q:       # q가 빌 때까지
        x, y = q.popleft()  # 왼쪽에서부터 꺼내온다. : queue의 성질, 뽑아 오는 것은 좌표값(x,y)
        for i in range(4):  # 상하좌우 4방향으로 이동하도록 설정됨
            nx = x + dx[i]  # 이동한 x 위치
            ny = y + dy[i]  # 이동한 y 위치
            
            # 이동한 위치가 토마토 격자 내부에 있다면(밖으로 나가지 않았다면)
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 0:
                # 토마토 격자(matrix)에서 토마토 상태 변경 ex) matrix[2][1] = matrix[3][1] +1
                matrix[nx][ny] = matrix[x][y] + 1 
                # 그렇게 이동한 곳에서도 익었을테니 다음 전파를 위해 queue에 저장
                q.append([nx, ny])
                
# 모든 로직이 끝났을 때 안 익은 토마토가 있는지, 다 익었다면 며칠이 걸렸는지 확인
def ripen_check():
    check = 0
    for i in range(h):      # 높이 h 만큼
        for j in range(w):  # 너비 w 만큼
            a = matrix[i][j]  # matrix[i][j]은 갈수록 갱신이 되었음. 그래서 뒤로 갈수록 a가 커진다.
            if a == 0:      # 모든 로직이 끝났는데도 0이 있다는건 막힌 부분이 있어서 익음이 전파 되지 못함. -1 출력후 종료
                print(-1)
                return
            check = max(check, a)  # 그렇지 않으면 다 익었다. check가 게속 갱신된다.
    print(check - 1)      # 예를들어 마지막날인 8일차에 전파된 토마토 자리에는 9가 들어 있음. 8이 아닌 이유는 1에서 시작했기 때문.

bfs_tomato(queue)
print(matrix)
ripen_check()



# arr = [[0 for col in range(M)] for row in range(N)]