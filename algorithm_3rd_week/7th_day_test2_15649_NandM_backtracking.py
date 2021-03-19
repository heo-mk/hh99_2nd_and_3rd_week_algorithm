# DFS_permutation(0, '')
# 순열을 백트레킹으로 설계
N, M = map(int, input().split())
N_sequence = [1+i for i in range(N)]  # N 길이 수열
visited = []

def DFS_permutation(depth):  # depth는 트리구조의 Level과 같은 것
    # 종료 조건 = depth 깊이만큼 탐색했을때
    if depth == M:
        for i in visited:
            print(i, end=' ')
        print()
        return

    for j in range(1, N+1):
        if j not in visited:  
            visited.append(j)
            print(visited)
            DFS_permutation(depth+1)   # 설정한 레벨까지 재귀로 간다.
            visited.pop()
            print(visited)
            # DFS_permutation(depth+1, result)

DFS_permutation(0)