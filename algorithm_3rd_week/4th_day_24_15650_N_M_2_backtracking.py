import sys
input = sys.stdin.readline
from itertools import combinations 

# N : 수열의 길이, M : 뽑아낸 수열의 길이
# N, M = map(int, input().split())
# N_sequence = [1 + i for i in range(N)]  # N 길이 수열
# visited = [False]* N  # 탐색 여부 체크
# out_sequences = []

# DFS_permutation(0, '')
# 순열 설계
N, M = map(int, input().split())
visited = []
test = []

def DFS_combination(depth):  # depth는 트리구조의 Level과 같은 것
    # 종료 조건 = depth 깊이만큼 탐색했을때
    if depth == M:
        for i in visited:
            print(i, end=' ')
        print()
        return

    for j in range(1, N+1):
        if j not in visited and j not in test: 
            visited.append(j)
            test.append(j)
            print(visited)
            DFS_combination(depth+1)   # 설정한 레벨까지 재귀로 간다.
            print(visited)
            visited.pop()
            print(visited)

DFS_combination(0)










# 중복되는 요소는 없되, 순서 상관 없이 뽑기 = 조합 : combination
# itertools 사용
import sys
input = sys.stdin.readline
from itertools import combinations
N, M = map(int, input().split())
C = combinations(range(1, N+1), M)
for i in range(len(C)):
    print(i)