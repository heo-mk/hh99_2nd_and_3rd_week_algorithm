# # baekjoon overtime 
# N = int(input())
# coordi_set = []

# for i in range(N):
# 	coordi = list(map(int, input().split()))
# 	coordi_set.append(coordi)

# for j in range(len(coordi_set) - 1):
# 	for k in range(len(coordi_set) - 1 - j):
# 		if coordi_set[k][1] > coordi_set[k+1][1]:
# 			coordi_set[k], coordi_set[k+1] = coordi_set[k+1], coordi_set[k]

# for m in range(len(coordi_set)):
# 	print(coordi_set[m])

# print()   

# new : sort method
import sys

N = int(sys.stdin.readline())
coordi_set = []

for i in range(N):
    coordi_set.append(list(map(int, sys.stdin.readline().split())))
print(coordi_set)
print()

for i in range(N):
    coordi_set[i][0], coordi_set[i][1] = coordi_set[i][1], coordi_set[i][0]
print(coordi_set)  
print()

coordi_set.sort()
print(coordi_set)
print()

for j in range(len(coordi_set)):
    coordi_set[j][0], coordi_set[j][1] = coordi_set[j][1], coordi_set[j][0]
    print(coordi_set[j][0], coordi_set[j][1])
