# 백준 1149 RGB 거리

arr = []
n = int(input())
for i in range(n):
	arr.append(list(map(int, input().split())))

for i in range(1, n): #arr을 dp테이블로 사용
	arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0] # 현재 집의 R(0)을 칠 할 때 최소 비용
	arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1] # 현재 집의 G(1)을 칠 할 때 최소 비용
	arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2] # 현재 집의 B(2)을 칠 할 때 최소 비용

min_result = min(min(arr[n-1][0], arr[n-1][1]), arr[n-1][2])
print(min_result)


#과정
## 처음
# 26 40 83
# 49 60 57
# 13 89 99

## 첫번째 반복 결과
# 26 40 83
# 89 86 83 <- 두번째 집까지 최소 비용
# 13 89 99

## 두번째 반복 결과
# 26 40 83
# 89 86 83
# 96 172 185 <- 세번째 집까지 최소 비용

# 96이 최소 비용
