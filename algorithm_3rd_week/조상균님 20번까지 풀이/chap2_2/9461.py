# 백준 9461 파도반 수열

table = [-1,1,1,1,2,2,3,4,5,7,9] + [-1] * 91
# P(N) = P(N-2) + P(N-3)

def pado(num):
	if table[num] != -1: # 이미 값이 있으면
		return table[num] # 테이블에 있는 값을 리턴
	else: # 미리 저장된 값이 없으면
		table[num] = pado(num-2) + pado(num-3) # 테이블에 값 저장
		return table[num] # 값 리턴


T = int(input())
result = []
for i in range(T):
	num = int(input())
	result.append(pado(num)) # 파도반 함수 실행하여 값을 리스트 저장

for s in result:
	print(s)
