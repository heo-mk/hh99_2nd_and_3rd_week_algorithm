import sys
input = sys.stdin.readline

# N : 영상 한변의 길이, 2의 배수로만 가능 2,4,8 .. 64, 128
N = int(input())

# 영상 데이터 구조 만들기
# 0, 1 입력
data_set = []
for i in range(N):
    # 아래와 같이 입력하면
    # 숫자를 공백없이 이렇게 11110000 입력해도
    # 숫자 하나씩 나눠져서 리스트에 입력됨 
    raw = list(map(int, input().rstrip()))
    data_set.append(raw)
    
print(data_set)

# 0이나 1만 있는 상태를 판별 : boolean으로 판별
def only_zero(table, n, x, y):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if table[i][j] == 1:
                return False
    return True

def only_one(table, n, x, y):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if table[i][j] == 0:
                return False
    return True

# 반으로 쪼개가면서 원하는 결과가 나올 때까지
# 계산 되도록 설정 = 분할정복 알고리즘
# x, y는 시작 기준 좌표
def half_cut(table, n, x, y):
    # 종료 조건시 출력 값 설정 : 0과 1이 출력식에 나오게 설정.
    if only_zero(table, n, x, y):
        return 0
    if only_one(table, n, x, y):
        return 1
    
    # 반으로 나눌 때 결과, 재귀로 구하기
    n = n//2
    # 출력형식은 '(좌상단 값 -> 우상단 값 -> 좌하단 값 -> 우하단 값)' 형식. 
    # 문자열로 변환하게 설정
    # 한 사분면에서 0과 1이 섞여 있으면 거기서 n//2로 쪼갠 것으로 들어가서 
    # '(좌상단 값 -> 우상단 값 -> 좌하단 값 -> 우하단)' 으로 출력 되는 재귀. 
    set_top_left = '(' + str(half_cut(table, n, x, y))          # ( 좌상단
    set_top_right = str(half_cut(table, n, x, y+n))             # 우상단
    set_bottom_left = str(half_cut(table, n, x+n, y))           # 좌하단
    set_bottom_right = str(half_cut(table, n, x+n, y+n)) +')'   # 우하단 )
    
    result = set_top_left + set_top_right + set_bottom_left + set_bottom_right
    return result

tree_result = half_cut(data_set, N, 0, 0)
print(tree_result)