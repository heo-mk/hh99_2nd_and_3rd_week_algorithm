import sys
input = sys.stdin.readline
n = int(input())

peoples_times = list(map(int, input().split()))   # 사람당 돈뽑는데 걸리는 시간 입력
peoples_times.sort()     # 오름차순으로 정렬 : 오름차순으로 정렬시 최소 시간 걸림

accumulated_time = list()
for i in range(len(peoples_times)):
    time_sum = sum(peoples_times[0:i+1])
    accumulated_time.append(time_sum)

print(sum(accumulated_time))
