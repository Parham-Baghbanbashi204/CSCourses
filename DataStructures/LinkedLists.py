#doubly linked lists
class DoubleLinkedList:
	size = 0 
	head = Node(None,None,None)
	tail = Node(None,None,None)
	

	class Node:
		data = None
		prevn = None
		nextn = None
		def __init__(self, data, prev, next):
			data = data
			prevn = prev
			nextn = next
		def return_data(self):
			return data


	def clear(self):
		trav = head
		while(trav != None):
			nextn = trav.nextn
			trav.prevn = trav.nextn
			trav.data = None
			trav = nextn
		head = tail = trav = None
		size = 0

	def size(self):
		return size

	def isEmpty(self):
		return size == 0 

	def add(element):
		addLast(element)

	def addFirst(self, element):
		if(isEmpty()):
			head = tail = Node(element, None, None)
		else:
			head.prevn = Node(element, None, None)
			head = head.prevn
		size += 1

	def addLast(element):
		if(isEmpty()):
			head = tail = Node(element, None, None)
		else:
			tail.nextn = Node(element, tail, None)
			tail = tail.nextn
		size += 1

	def peekFirst(self):
		if(isEmpty): raise RuntimeError("Empty List")
		return head.data








