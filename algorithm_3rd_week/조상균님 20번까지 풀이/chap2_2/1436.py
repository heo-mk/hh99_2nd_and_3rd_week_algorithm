# 백준 1436 영화감독 숌

n = int(input())

count = 0 # 666이 들어간거 카운트
num = 0 # n번째를 찾을 때까지 올라가는 숫자
while True:
	if "666" in str(num): #만약 666이 num 안에 있다면
		count += 1 # 카운트 +1
	if count == n: # 만약 찾으려는 번째와 같으면
		break # 반복 끝
	num += 1 # 숫자 증가

print(str(num))
