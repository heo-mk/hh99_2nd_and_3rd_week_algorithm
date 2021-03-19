# class MaxHeap:
# 	def __init__(self):
# 		self.items = [None]
# 	def insert(self, value):
# 		self.items.append(value)
# 		current_index = len(self.items) - 1
# 		while current_index > 1:
# 			parent_index = current_index // 2
# 			if self.items[parent_index] < self.items[current_index]:
# 				self.items[parent_index], self.items[current_index] = self.items[current_index], self.items[parent_index]
# 				current_index = parent_index
# 			else:
# 				break

# max_heap = MaxHeap()
# max_heap.insert(3)
# max_heap.insert(4)
# max_heap.insert(2)
# max_heap.insert(9)
# print(max_heap.items)

class MaxHeap:
	def __init__(self):
		self.items = [None]
	def insert(self, value):
		self.items.append(value)
		current_index = len(self.items) - 1  # 가장 마지막 것

		while current_index > 1:
			parent_index = current_index // 2
			if self.items[parent_index] < self.items[current_index]:
				self.items[parent_index], self.items[current_index] = self.items[current_index], self.items[parent_index]
				current_index = parent_index
			else:
				break

	def delete(self):
		self.items[1], self.items[-1] = self.items[-1], self.items[1]
		prev_max = self.items.pop()
		current_index = 1

		while current_index <= len(self.items) - 1:
			left_child_index = current_index * 2
			right_child_index = current_index * 2 + 1
			max_index = current_index

			if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
				max_index = left_child_index
			if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
				max_index = right_child_index
			if max_index == current_index:
				break

			self.items[current_index], self.items[max_index] = self.items[max_index], self.items[current_index]
			current_index = max_index

		return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)
print(max_heap.delete())
print(max_heap.items)