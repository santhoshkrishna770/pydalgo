# Stack is a ADT which follows LIFO principle means last in first out. 


class Stack:
	""" Stack class creates stack objects """
	def __init__(self, data=None):
		self.data = data
		self.ls = []

	def push(self, key):
		""" doc string """
		if self.data is None:
			self.data = key
			self.ls.append(self.data)

	def pop(self):
		""" doc string """
		if self.data is None:
			return "Stack is empty"
		else:
			return self.ls[-1]
			self.ls.pop()

	def top(self):
		""" doc string """
		return self.ls[0]

	def isEmpty(self):
		return bool(self.ls)