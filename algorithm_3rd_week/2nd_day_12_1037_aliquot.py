import sys
input = sys.stdin.readline
n = int(input())
aliquot = list(map(int, input().split()))

# aliquot.sort()
# min_aliquot = aliquot[0]
# max_aliquot = aliquot[-1]

min_aliquot = min(aliquot)
max_aliquot = max(aliquot)

number = min_aliquot * max_aliquot
print(number)

# 16 : 2 x 8 = 16
# 20 : 2 x 10 = 20
# 75 : 3 X 25 = 75