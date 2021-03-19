from collections import Counter
import sys
N = int(input())

arr =[]
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

# 평균
avg = round(sum(arr)/len(arr))
# 중간값
median = arr[len(arr)//2]
# 최빈값
c = Counter(arr)
mode_list=c.most_common(2)
mode = 0
if mode_list[0][1]!=mode_list[-1][1]:
    mode = mode_list[0][0]
else:
    mode = mode_list[-1][0]
#범위
num_range = max(arr)-min(arr)

print(avg)
print(median)
print(mode)
print(num_range)