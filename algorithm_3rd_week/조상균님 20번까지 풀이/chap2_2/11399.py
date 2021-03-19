# 백준 11399 ATM

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

minute = 0
before = 0
for i in arr:
	minute += i + before
	before += i

print(minute)

# 대기열이 1 2 3 4 5 일 때
# 1번째 손님은 1분
# 2번째 손님은 3분(이전손님:1+자기꺼:2)
# 3번째 손님은 6분(이전손님:3+자기꺼:3)
# 4번째 손님은 10분(이전손님:6+자기꺼:4)
# 5번째 손님은 15분(이전손님:10+자기꺼:5)
