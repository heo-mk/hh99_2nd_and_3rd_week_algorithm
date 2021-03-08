# There must be at least one prime number btw M and N.
# m, n = input().split()
# M, N = int(m), int(n)
# all_list = list(range(M, N+1))

# for i in range(M, N+1):
#     for j in range(2, i):
#         if i % j == 0 :
#             break
#         print(i)

# all_list = list(range(10, 14))
            
# for i in all_list:
# 	# print(i)
# 	# print()
# 	for j in range(2, i):
# 		# print(j)
# 		# print(i)
# 		if i % j == 0:
#     			print(i)
            # all_list.remove(i)
	# print()
    #         # print(all_list)

# for i in all_list:
#     print(i)

all_list = list(range(10, 14))
print(all_list)
            
for i in all_list:
	for j in range(2, i):
		if i % j == 0:
			break
	all_list.remove(i)

for k in all_list:
	print(k)




