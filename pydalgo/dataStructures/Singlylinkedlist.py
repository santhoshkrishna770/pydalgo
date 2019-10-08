# Implementation of Singly Linked list 
# Class Node: It creates node which is used by Class SinglyLinkedList
#
# node = Node() is not a member of singlylinkedlist class just because we have to create multiple Node instance per one
# singlyLinkedList. Node instance is created only when user enter a data


class Node:

	def __init__(self,key=None):
		self.key=None
		self.next=None


class SinglyLinkedList(object):
	"""docstring for SinglyLinkedList"""
	def __init__(self):
		"""DocString"""

		self.head = None

	def pushFront(self,key):
		"""DocString"""
		pass

	def topFront(self):
		"""No parameter taken return"""
		if self.head is None:
			return "List is Empty"
		return self.head.key

	def popFront(self):
		"""doc string"""
		pointer = self.head
		if self.head:
			self.head = self.head.next
		else:
			print("list is empty")
		del(pointer)

	def pushBack(self,key):
		""" doc string"""
		pass

	def topBack(self):
		""" doc string"""
		pass

	def popBack(self):
		""" doc string """
		pass

	def find(self, key):
		"""doc string """
		pass

	def erase(self,key):
		"""doc string"""
		pass

	def isEmpty(self):
		"""doc string"""
		pass

	def addBefore(self,key):
		"""doc string"""
		pass

	def addAfter(self,key):
		"""doc string"""
		pass

	def __str__(self):
		"""doc string"""
		pass

	def __repr__(self):
		"""doc string"""
		pass

s = SinglyLinkedList()
s.pushFront(1)
print(s.node.key)
s.pushFront(2)
print(s.node.key)