# 백준 2839 설탕 배달

kg = int(input())

count = 0

while True: # 총 무게가 다 없어질 떄 까지 반복
	if kg % 5 == 0: # 5kg으로 나누어 떨어지면
		count += kg // 5 #5kg으로 다 채움
		break
	else: # 5로 나눠떨어지지 않으면 3kg 봉지 늘리기
		kg -= 3
		count += 1
	if kg == 0:
		break
	if kg < 0: # 봉지가 안나누어 떨어져서 0미만으로 떨어지면
		count = -1
		break
print(count)
