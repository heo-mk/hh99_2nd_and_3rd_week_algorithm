dr = [0,1,0,-1]
dc = [1,0,-1,0]

def DFS(row,col):
    global cnt
    if MAP[row][col]=='0':
        return 0
    
    # count 처리하는 방법을 조금 더 숙지 할 필요가 있음!!
    MAP[row][col] ='0'
    cnt+=1
    for i in range(4):
        new_row = row+dr[i]
        new_col = col+dc[i]        
        if 0<=new_row<N and 0<=new_col<N and MAP[new_row][new_col]=='1':
            DFS(new_row,new_col)

# 초기화 하는 부분
N = int(input())
MAP = []
for _ in range(N):
    row = list(input())
    MAP.append(row)

# count하기 위한 부분
houses =[]
cnt = 0
for i in range(N):
    for j in range(N):
        if MAP[i][j]=='1':
            cnt = 0
            DFS(i,j)
            houses.append(cnt)

### 정답 
print(len(houses))
houses.sort()
for house in houses:
    print(house)