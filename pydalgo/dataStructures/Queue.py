


class Queue:
	""" doc string """
	def __init__(self,head=None):
		self.head = head
		self.ls = []

	def enqueue(self,key):
		""" doc string """
		if self.head is None:
			self.head = key
		self.ls.append(self.head)

	def dequeue(self, key):
		""" doc string """
		if self.head is None:
			return "Queue is empty"
		else:
			return self.ls[0]
			self.ls.pop(0)

	def top(self):
		""" doc string """
		return self.head

	def isEmpty(self):
		""" doc string """
		return bool(self.ls)