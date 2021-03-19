import sys
input = sys.stdin.readline

N = int(input())
attempts = []
# 1 이상 자기 미만 범위내 모든 숫자 검사 : brute force
for j in range(1, N+1):
    temp = j
    string = str(j)  '123' -> 1 2 3
    for k in string: # 이중 for문이 되어서 비효율적
        temp += int(k)
    attempts.append(temp)  # 각각의 j가 만드는 숫자들의 모임
    
if N not in attempts:   # 생성된 숫자중 N과 같은 것이 없다 
    print(0)            # N은 생성자가 없는 셀프넘버
else:                    
    index_ = attempts.index(N)  # 생성된 숫자가 N과 같다면
    print(index_ + 1)           # 그때 index + 1 = N의 가장 작은 생성자
    

# 짧은 코드 #
N = int(input())
result = 0
# 1부터 N까지 모조리 조사.
for i in range(1, N+1):  # for문 한번으로 끝내서 효율적
    ciphers = list(map(int, str(i))) # 자릿수들을 쪼개서 모은 리스트
    result = i + sum(ciphers)        # 자기 자신과 쪼개 놓은 자릿수들의 합을 더한다.
    if result == N:  # 생성자 중에서 가장 작은 숫자 등장.
        print(i)
        break        # 생성자 중에서 가장 작은 것을 찾았으므로 끝낸다.
    
    if i == N:       # N은 생성자가 없는 숫자 == 셀프넘버
        print(0)
    