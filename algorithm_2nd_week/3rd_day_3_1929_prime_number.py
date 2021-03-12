# # There must be at least one prime number btw M and N.
# # m, n = input().split()
# # M, N = int(m), int(n)
import sys

m, n = sys.stdin.readline().split()
M, N = int(m), int(n)
all_list = list(range(M, N+1))

# all_list = list(range((map(int, sys.stdin.readline().split()))))
print(all_list)
            
for i in all_list:
	for j in range(2, int(i**0.5)+1):
		if i % j == 0:
			break
	all_list.remove(i)

for k in all_list:
	print(k)


# 쉬운 풀이
import sys

all_list = list(map(int, sys.stdin.readline().split()))
for i in range(all_list[0], all_list[1] + 1):
    if i == 0:
        check = False
    elif i > 1:
        check = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = False
                break
        if check:
            print(i)