# # 1st
import sys
N=int(sys.stdin.readline())
li=[]

for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    li[i][0],li[i][1]=li[i][1],li[i][0]

li.sort()
for i in range(N):
    li[i][0],li[i][1]=li[i][1],li[i][0]
    print(li[i][0], li[i][1])


# 2nd
import sys
n = int(sys.stdin.readline())
so = []

for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))

print(so)

so.sort(key=lambda x: (x[1], x[0]))
for i in so:
    print(i[0], i[1])
