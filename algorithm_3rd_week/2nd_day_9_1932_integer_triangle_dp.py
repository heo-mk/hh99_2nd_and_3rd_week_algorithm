N = int(input())  # 삼각형 층수

tri_regular = []  # 삼각형의 각 자리에 있는 숫자 담을 리스트
for i in range(N):  
    tri_regular.append(list(map(int, input().split())))
# max_total = 꼭대기값

print(tri_regular)

# dynamic programming 시행
# 첫줄은 갱신 안되므로, 두번째 줄부터 갱신시작.
# 그래서 range(1, N)
for i in range(1, N):
    ln = len(tri_regular[i])
    for j in range(ln): 
        if j == 0:     # 맨 왼쪽 모서리 따라서 갈 때, memoization
            tri_regular[i][j] += tri_regular[i-1][0]
            continue
        elif j == i:   # 맨 오른쪽 모서리 따라서 갈 때, memoization
            tri_regular[i][j] += tri_regular[i-1][-1]
            continue
        else:          # 그외의 경우
            tri_regular[i][j] += max(tri_regular[i-1][j-1], tri_regular[i-1][j])

# 최대값은 마지막층에 누적된 수 중에서 최댓값, 마지막층의 index == N-1
max_value = max(tri_regular[N-1])
print(max_value)


# 금교석님식 파일 소환 적용해서 풀기