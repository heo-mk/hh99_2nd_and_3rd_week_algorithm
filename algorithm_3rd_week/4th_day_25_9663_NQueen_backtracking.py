# 교수님 방식 : 결과 출력이 되지 않음
# import sys
# input = sys.stdin.readline
# N = int(input())

# # result = []
# def n_queens(level, column): # 
#     n = len(column) - 1    # index는 0 부터 시작이므로.
#     if promising(level, column):
#         if level == column:
#             # result.append(column[1:n+1])
#             print(column[1:n+1])
#     else:
#         for j in range(1, n+1):
#             column[level+1] = j
#             n_queens(level+1, column)

# def promising(level, column):
#     k = 1       # k, level는 행의 번호 = level
#     flag = True
#     while k < level and flag:
#         # 같은 열에 있는가 or 같은 대각선에 있는가
#         if column[level] == column[k] or abs(column[level] - column[k]) == (level - k):
#             flag = False
#         k += 1
#     return flag

# column = [0] * (N + 1)
# n_queens(0, column)
# # print(len(result))


import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
a, b, c = [[False]*N, [False]*(2*N-1), [False]*(2*N-1)]
# a = 같은 열, b = 오른쪽 상단으로 가는 대각선
# c = 왼쪽 상단으로 가는 대각선
# 이 조건들에 걸리면 Queen 자리가 될 수 없음 

def nqueen(level):
    global cnt 
    if level == N:
        cnt += 1
        return
    
    # 재귀 설정
    # for j in range(N):
    #     if not (a[j] or b[level+j] or c[level-j+N-1]):
    #         a[j] = b[level+j] = c[level-j+N-1] = True
    #         nqueen(level + 1)
    #         a[j] = b[level+j] = c[level-j+N-1] = False
    
    for j in range(N):
        if not (a[j] or b[level+j] or c[level-j]):   # 하나라도 False(거짓)이라면
            a[j] = b[level+j] = c[level-j] = True
            nqueen(level + 1)
            print(a, b, c)
            a[j] = b[level+j] = c[level-j] = False

nqueen(0)
print(cnt)