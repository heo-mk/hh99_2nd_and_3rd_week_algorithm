class LinkedList:
	def __init_(self, value):
		self.head = Node(value)

	def append(self, value):
		cur = self.head
		while cur.next is not None:
			cur = cur.next
		cur.next = Node(value)

linked_list = LinkedList(5)
liked_list.append(12)
liked_list.append(8)

