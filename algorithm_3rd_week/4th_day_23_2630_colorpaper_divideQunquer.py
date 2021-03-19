import sys
input = sys.stdin.readline

# N : 전체 종이 한변의 길이, 2의 배수로만 가능 2,4,8 .. 64, 128
N = int(input()) 

# 색종이 사각형 만들기
# 흰색:0, 파란색:1
square_papers = []
for i in range(N):
    raw = list(map(int, input().split()))
    square_papers.append(raw)

print(square_papers)
print(square_papers[0:N][0:N])

# paper_list : 색종이사각형, n : 사각형 한변의 길이
# 분할점령 : 종료조건 + 재귀

# 1st_종료조건, 
# 흰색:0, 파란색:1
# table = 색종이 위치 정보
# n : 색종이 한 변의 길이
# x, y : 사각형 왼쪽 상단 좌표 = 시작 좌표
def blue_end(table, n, x, y):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if table[i][j] == 0:
                return False
    return True

def white_end(table, n, x, y):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if table[i][j] == 1:
                return False
    return True

# 반으로 나눌때 조건
# 흰색:0, 파란색:1
# x, y는 시작 기준 좌표
def half_cut(table, n, x, y):
    # 종료 조건
    if blue_end(table, n, x, y):
        return [0, 1]
    if white_end(table, n, x, y):
        return [1, 0]
    
    # 반으로 나눌 때 결과, 재귀로 구하기
    n = n//2
    total = [0, 0]
    box_top_left = half_cut(table, n, x, y)
    box_top_right = half_cut(table, n, x, y+n)
    box_bottom_left = half_cut(table, n, x+n, y)
    box_bottom_right = half_cut(table, n, x+n, y+n)
    
    # white 결과 끼리 묶기
    total[0] = box_top_left[0] + box_top_right[0] + box_bottom_left[0] + box_bottom_right[0]
    # blue 결과 끼리 묶기
    total[1] = box_top_left[1] + box_top_right[1] + box_bottom_left[1] + box_bottom_right[1]

    return total


# 검사 시행
result = half_cut(square_papers, N, 0, 0)

print(result[0])
print(result[1])





# count_0 = 0; count_1 = 0
# def paper_divide(paper_list, n):
#     # 가장 바닥 조건
#     if n == 1:
#         if paper_list[0][0] == 0
#             count_0 = paper_list[0][0]
#         elif paper_list[0][0] == 1
#             count_1 = paper_list[0][0]
#             return (count_0, count_1)

#     mid = n // 2
#     group_top_left = paper_list[x:x+mid][y:y+mid]
#     group_top_right = paper_list[x:x+mid][mid:]
#     group_down_left = 
#     group_down_right = 

#         return count_0,\n count_1
    
#     ln = len(paper_list)
#     for i in range(ln):
#         paper_list[0:ln][0:ln] == 0 or paper_list[0:ln][0:ln] == 1:
#             if paper_list[0:ln][0:ln] == 0:
#                 print(1)
#             else:
#                 print(0)