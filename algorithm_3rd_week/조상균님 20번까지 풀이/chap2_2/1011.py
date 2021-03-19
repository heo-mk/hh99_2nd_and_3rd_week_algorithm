# 백준 1011 Fly me to the Alpha Centauri

#입력
n = int(input())
cases = []
for i in range(n):
	cases.append(list(map(int, input().split())))


result = [] #결과 저장 배열
for case in cases:
	target = case[1] - case[0] # 이동해야 할 거리
	count = 0
	if target == 0: # 0일 때 결과
		count = 0
	elif target == 1: # 1일 때 결과
		count = 1
	else:
		num = 1 # 수열 증가
		re = 0 # 한번 나왔는지 두번나왔는지
		compare = 0 # 더해지면서 이동거리와 비교
		while compare < target:
			if re == 0: # 증가하고 처음일 때
				re = 1 #수열이 나왔다는 표시
				compare += num # 비교 거리 증가
			else: # 증가하고 이전에 한번 나오면 같은 차이로 또 증가
				re = 0
				compare += num # 비교 거리 증가
				num += 1 # 다음 수열 폭 증가
			count += 1
	result.append(count)

for st in result:
	print(st)


# 수열 1 2 3 5 7 10 13 17 21
#      1 1 2 2 3  3  4  4 규칙적 증가
# 이동거리 1 = > 1 = 1

# 이동거리 2 = > 1 1 = 2

# 이동거리 3 = > 1 1 1 = 3
# 이동거리 4 = > 1 2 1 = 3

# 이동거리 5 = > 1 2 1 1 or 1 1 2 1 = 4
# 이동거리 6 = > 1 2 2 1 = 4

# 이동거리 7 = > 1 2 2 1 1 or 1 1 2 2 1 = 5
# 이동거리 8 = > 1 2 2 2 1 = 5
# 이동거리 9 = > 1 2 3 2 1 = 5

# 이동거리 10 = > 1 2 3 2 1 1 = 6
# 이동거리 11 = > 1 2 3 2 2 1 = 6
# 이동거리 12 = > 1 2 3 3 2 1 = 6

# 이동거리 13 = > 1 2 3 3 2 1 1 = 7
# 이동거리 14 = > 1 2 3 3 2 2 1 = 7
# 이동거리 15 = > 1 2 3 3 3 2 1 = 7
# 이동거리 16 = > 1 2 3 4 3 2 1 = 7

# 이동거리 17 = > 1 2 3 4 3 2 1 1 = 8
# 이동거리 18 = >

# 이동거리 20 = > 1 2 3 4 4 3 2 1 = > 8

# 21 = > 1 2 3 4 4 3 2 1 1 = > 9
# 24 = > 1 2 3 4 4 4 3 2 1 = > 9
# 25 = > 1 2 3 4 5 4 3 2 1 = > 9
