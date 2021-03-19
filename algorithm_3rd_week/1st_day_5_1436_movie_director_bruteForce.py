# brute force 알고리즘 사용
# 금교석님 방식 : 내림차순
n = int(input())    # n번째 영화.
m = 666

while n:       # n이 0이 되기 전
    if '666' in str(m):   # 핵심 아이디어. if ___ in ___: 형식을 잘 이해하자.
        n -= 1
        print(n)
    m += 1
    print(m)

print(m-1)   # 영화 제목에 들어간 숫자 출력.



# 조상균님 방식 : 오름차순
n = int(input())
count = 0   # 666 들어간 숫자의 순서를 센다
num = 665   # 665 다음 숫자부터 666이 등장.
while True:
    if '666' in str(num): # 문자열화 한 숫자에서 666이 있다면
        count += 1        # 횟수를 추가한다.       
    if count == n:  # 666이 n회 만큼 나오면 종료.
        break
    num += 1        # 666이 원하는 횟수만큼 나올때까지 숫자를 1씩 늘리면서 반복.

print(num)   # 영화 제목에 들어간 숫자 출력

## 배운 점 ## 
## brute force를 구현하기 위해서
## 모든 경우를 검사하는 알고리즘
## 구현법을 익힘. 