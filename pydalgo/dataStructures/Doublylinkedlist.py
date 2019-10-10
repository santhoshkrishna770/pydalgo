# Implementation Code for Doubly linked list
# 2 classes are required - Node: To create nodes for linked list
#                          DoublylinkedList: To create a list object

# pointers required:: head - to point to the first element always
#                     tail - to point to the last element always
#                     current_node: To track movement

# The Node class contains data, next, prev




### Errors : 
#    After popfront the last element there is an error like " None type object have no attribute 'prev' "
#    This should be catch and print:: list is empty
#



class Node:
	""" creates nodes of a linked list """
	def __init__(self,key=None):
		self.key = key
		self.next = None
		self.prev = None


class DoublylinkedList:
	""" The class to create linked list, a list of nodes which contain data, pointer to next and previous node """
	def __init__(self,head=None):
		self.head=head

	def pushFront(self,key):
		""" This method adds element to the top of the list, the inserted element will occupy index 0 """
		node = Node(key)
		if self.head is None:
			self.head = node
			node.prev = self.head

		else:
			node.next = self.head
			self.head = node
			node.prev = self.head

	def topFront(self):
		""" Returns the first element """
		return self.head.key

	def popFront(self):
		""" remove the first element in the list """
		current_node = self.head
		if self.head is None:
			return "List is empty"
		else:
			current_node.next.prev = self.head
			self.head = self.head.next

	def pushBack(self,key):
		""" create a node and push it to the end of the list """
		current_node = self.head
		node = Node(key)
		if self.head is None:
			node.prev = self.head
			self.head = node
		else:
			while current_node.next:
				current_node = current_node.next
			current_node.next = node
			node.prev = current_node

	def topBack(self):
		""" return the last element on the list """
		current_node = self.head
		if self.head is None:
			return "List is empty"
		else:
			while current_node.next:
				current_node = current_node.next
			return current_node.key


	def addBefore(self,node_key,key):
		""" inserts a node before given a node_key. First find the given key in the liked list and 
		 then insert before the node """
		current_node = self.head
		node = Node(key)
		if self.head is None:
			return "List is empty"
		else:
			while current_node:
				if current_node.key == node_key:
					
					break
				current_node = current_node.next


	def addAfter(self,node_key,key):
		""" inserts a node after given a node_key. First find the given key in the liked list and 
		 then insert after the node """
		current_node = self.head
		node = Node(key)
		if self.head is None:
			return "List is empty"
		else:
			while current_node:
				if current_node.key == node_key:
					node.next = current_node.next
					current_node.next.prev = node
					node.prev = current_node
					break
				current_node = current_node.next

	def isEmpty(self):
		return bool(self.head)

	def find(self,key):
		pass

	def erase(self,key):
		pass

	def __str__(self):
		pass

	def __repr__(self):
		pass




s = DoublylinkedList()
s.pushFront(1)
print(s.topFront())
s.pushFront(2)
print(s.topFront())
s.pushFront(3)
print(s.topFront())
s.popFront()
print(s.topFront())
s.popFront()
print(s.topFront())
s.pushBack(4)
print(s.topBack())
s.pushBack(5)
print(s.topBack())
print(s.topFront())