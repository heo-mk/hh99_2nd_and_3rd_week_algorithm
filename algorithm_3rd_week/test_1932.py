import sys
sys.stdin = open('test_1932.txt','rt')

#초기화
N = int(input())
MAP =[]
for _ in range(N):
    row = list(map(int,input().split()))
    MAP.append(row)

# 첫번째 줄 마지막 줄 누적합 해주기
for i in range(1,N):
    MAP[i][0] += MAP[i-1][0]
    MAP[i][-1]+=MAP[i-1][-1]


# DP로풀기
for i in range(1,N):
    for j in range(1,len(MAP[i])-1):
        MAP[i][j] += max(MAP[i-1][j],MAP[i-1][j-1])

print(max(MAP[N-1]))