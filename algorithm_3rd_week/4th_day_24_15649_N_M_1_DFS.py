# # 중복되는 요소는 없되, 가능한 순서를 모두 찾기 = 순열 : perrmutation
# 불행히도 이해가 안 되는 풀이
# import sys
# input = sys.stdin.readline

# # N : 수열의 길이, M : 뽑아낸 수열의 길이
# N, M = map(int, input().split())
# N_sequence = [1 + i for i in range(N)]  # N 길이 수열
# visited = [False]* N  # 탐색 여부 체크 
# out_sequences = []

# def DFS_permutation(depth, n, m):
#     if depth == m:  # 탈출조건 : M개만큼 탐색하면 끝낸다.
#         print(' '.join(map(str, out_sequences)))
#         return

#     for i in range(n):
#         if visited[i]:
#             continue
        
#         visited[i] = True
#         out_sequences.append(i+1)
#         print(out_sequences)
#         print(visited)

#         DFS_permutation(depth + 1, n, m)
#         out_sequences.pop()
#         print(out_sequences)
#         print(visited)
#         visited[i] = False

# print(DFS_permutation(0, N, M))


# # 교석님, 상균님에게 과외 받고 푼 방식
# import sys
# input = sys.stdin.readline

# N : 수열의 길이, M : 뽑아낸 수열의 길이
# N, M = map(int, input().split())
# N_sequence = [1 + i for i in range(N)]  # N 길이 수열

# def DFS_permutation(depth, result):  # depth는 트리구조의 Level과 같은 것
#     # 종료 조건 = depth 깊이만큼 탐색했을때
#     if depth == len(N_sequence): 
#         print(result)
#         return
#     else:
#         DFS_permutation(depth+1, result + str(N_sequence[depth]))
#         DFS_permutation(depth+1, result)
#         # for i in range(len(N_sequence)):
#             # DFS_permutation(depth+1, result + str(N_sequence[depth]))
#             # DFS_permutation(depth+1, result)

# DFS_permutation(0, '')

# a = [1,2,3,4]
# def DFS_permutation(depth, result):  # depth는 트리구조의 Level과 같은 것
#     # 종료 조건 = depth 깊이만큼 탐색했을때
#     if depth == 2: 
#         print(result)
#         return
    
#     else:
#         for i in range(len(a)):
#             DFS_permutation(depth + 1, result + str(a[i]))


#         # DFS_permutation(depth + 1, result + str(a[0]))
#         # DFS_permutation(depth + 1, result + str(a[1]))
#         # DFS_permutation(depth + 1, result + str(a[2]))
#         # DFS_permutation(depth + 1, result + str(a[3]))


# DFS_permutation(0, '')
# 순열 설계
N, M = map(int, input().split())
N_sequence = [1 + i for i in range(N)]  # N 길이 수열
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



# # 중복되는 요소는 없되, 가능한 순서를 모두 찾기 = 순열 : perrmutation
# # itertools 사용
# import sys
# input = sys.stdin.readline
# from itertools import permutations
# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)
# print(P)
# for i in P:
#     print(*i)