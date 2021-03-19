import heapq

# def heap_sort(nums):
# 	heap = []
# 	for num in nums:
# 		heapq.heappush(heap, num)

# 	sorted_nums = []
# 	while heap:
# 		sorted_nums.append(heapq.heappop(heap))
# 	return sorted_nums

# print(heap_sort([4, 1, 7, 3, 8, 5]))

# nums = [4, 1, 7, 3, 8, 5]
# heap = []



# for num in nums:
# 	heapq.heappush(heap, (-num, num))

# while heap:
# 	print(heapq.heappop(heap)[1])

# print(heap)



# def kth_smallest(nums, k):
# 	heap = []
# 	for num in nums:
# 		heapq.heappush(heap, num)

# 	kth_min = None
# 	for i in range(k):
# 		kth_min = heapq.heappop(heap)
# 	print(kth_min)
# 	return kth_min

# print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

queue = []

heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])
print(queue)

for i in range(len(queue)):
	print(heapq.heappop(queue))
