import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
integers = []
for i in range(N):
    integers.append(int(input().rstrip()))

integers.sort()
print(integers)

# 산술평균
avg = round(sum(integers)/len(integers))
print(avg)

# 중앙값
center_val = integers[len(integers)//2]
print(center_val)
print()

# 최빈값
c = Counter(integers)
print(c)
mode_list = c.most_common(2)
print(mode_list)
print()
mode = 0
if mode_list[0][1] != mode_list[1][1]:
    mode = mode_list[0][0]
else:
    mode = mode_list[-1][0]
print(mode)

# 범위
range_ = abs(integers[0] - integers[-1])
print(range_)
