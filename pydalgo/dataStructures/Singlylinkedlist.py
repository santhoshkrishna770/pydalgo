# Implementation of Singly Linked list 
# Class Node: It creates node which is used by Class SinglyLinkedList
#
# node = Node() is not a member of singlylinkedlist class just because we have to create multiple Node instance per one
# singlyLinkedList. Node instance is created only when user enter a data


# 3 pointers are declared 1. head: points to first node always
#                         2. tail: points to last node always
#                         3. current_node: varies position as per requirements

class Node(object):

	def __init__(self,key=None):
		self.key=key
		self.next=None


class SinglyLinkedList(object):
	"""docstring for SinglyLinkedList"""
	def __init__(self,head=None):
		"""Initializing a linked list with the valid argument, if nothing given default is None. So the head points to None
			Otherwise it points to the node.
		"""

		self.head = head
		
	def pushFront(self,key):
		"""When a element named key is pushed then it create a node to which the head pointer points to"""
		node = Node(key)
		#print(node.key)
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
 
	def topFront(self):
		"""No parameter taken return"""
		if self.head is None:
			return "List is Empty"
		return self.head.key

	def popFront(self):
		"""doc string"""
		if self.head:
			self.head = self.head.next
		else:
			print("list is empty")

	def pushBack(self,key):
		"""Find the last element and then add node after that"""
		node = Node(key)
		current_node = self.head
		if self.head is None:
			self.head = node
		else:
			while current_node.next:
				current_node = current_node.next
			current_node.next = node

	def topBack(self):
		""" returns the last element of the linked list"""

		current_node = self.head
		if self.head is None:
			return "list is empty"
		else:
			while current_node.next:
				current_node = current_node.next
			return current_node.key

	def printD(self):
		current_node = self.head
		while current_node.next:
			print(self.head.key)
			current_node = current_node.next

	def popBack(self):
		""" Pop up the end node """
		current_node = self.head

		if self.head is None:
			print("list is empty")
			return None

		else:
			while current_node.next.next:
				current_node = current_node.next
			#return current_node.next.key
			current_node.next = None
			



	def find(self, key):
		"""To search the first occurance of the key """
		current_node = self.head
		c=0
		if self.head is None:
			return "List is empty"
		else:
			while current_node.next:
				c+=1
				if current_node.key == key:
					return c
					break
				current_node = current_node.next




# 	def erase(self,key):
# 		"""doc string"""
# 		pass

# 	def isEmpty(self):
# 		"""doc string"""
# 		pass

# 	def addBefore(self,key):
# 		"""doc string"""
# 		pass

# 	def addAfter(self,key):
# 		"""doc string"""
# 		pass

# 	def __str__(self):
# 		"""doc string"""
# 		pass

# 	def __repr__(self):
# 		"""doc string"""
# 		pass

s = SinglyLinkedList()
s.pushFront(1)

print("1______")
print(s.topFront())
print(s.topBack())
s.pushFront(2)
print("2___1_____")
print(s.topFront())
print(s.topBack())
s.pushBack(3)
s.pushBack(4)
s.pushFront(5)
print("5__2___1___3__4")

print(s.topFront())
print(s.topBack())
s.popBack()
print("5__2___1___3__")
print(s.topFront())
print(s.topBack())
s.popFront()
print("2___1_____3")
print(s.topFront())
print(s.topBack())
print(s.find(3))

# print(s.topFront())
# print(s.topBack())


# print("I am 2 and key is {}".format(s.head.key))
# print("I am 2 and next key is {}".format(s.head.next.key))
# s.pushFront(3)
# print("I am 3 and key is {}".format(s.head.key))
# print("I am 3 and next key is {}".format(s.head.next.key))
# s.pushFront(4)
# print("I am 4 and key is {}".format(s.head.key))
# print("I am 4 and next key is {}".format(s.head.next.key))
# s.pushFront(5)
# print("I am 5 and key is {}".format(s.head.key))
# print("I am 5 and next key is {}".format(s.head.next.key))