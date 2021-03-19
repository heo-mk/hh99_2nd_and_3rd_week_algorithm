# 백준 1932 정수 삼각형

arr = []
n = int(input())

for i in range(n):
	arr.append(list(map(int, input().split())))

for i in range(1,n):
	for j in range(i + 1):
		if j == 0: # 삼각형의 맨 앞은 이전의 맨 앞에꺼만 가져올 수 있음
			arr[i][j] += arr[i-1][0]
		elif j == i:  # 삼각형의 맨 뒤은 이전의 맨 뒤에꺼만 가져올 수 있음
			arr[i][j] += arr[i-1][j-1]
		else:
			arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[n-1]))
