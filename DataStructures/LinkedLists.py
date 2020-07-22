#doubly linked lists
"""
class Node():
		def __init__(self, data, previousNode, nextNode):
			self.data = data
			self.nextNode = nextNode
			self.previousNode = previousNode

		def toString(self):
			return str(self.data)
"""

class DoubleLinkedList():
	class Node():
		def __init__(self, data, previousNode, nextNode):
			self.data = data
			self.nextNode = nextNode
			self.previousNode = previousNode

		def toString(self):
			return str(self.data)

	
	def __init__(self):
		self.size = 0
		self.head = self.Node(None, None, None) 
		self.tail = self.Node(None, None, None) 

	
	def size(self):
		return self.size

	def isEmpty(self):
		return self.size == 0 

	def clearList(self):
		trav = self.head
		while trav != None:
			next = trav.nextNode
			trav.previousNode = trav.nextNode = None
			trav.data = None
			trav = next
		head = tail = trav = None
		size = 0 

	def addLast(self, element):
		if self.isEmpty():
			self.head = self.tail = self.Node(element,None,None)
		else:
			if self.size > 0 and self.size < 2:
				self.head.nextNode = self.tail

				print(self.head.nextNode, "<-- next node in head")
			#create new node at end of list
			self.tail.nextNode = self.Node(element, self.tail, None)
			#move tail pointer form current node to next node
			self.tail = self.tail.nextNode
		

			
		self.size += 1

	def addFirst(self, element):
		if self.isEmpty():
			self.head = tail = self.Node(element, None, None)
		else:
			#create node at start of list
			self.self.head.previousNode = self.Node(element, None, self.head)
			#move head pointer form current node to new node
			self.head = self.head.priviousNode
		self.size += 1


	def add(self, element):
		self.addLast(element)

	def peekFirst(self):
		if self.isEmpty():
			raise RuntimeError("Empty List")
		return self.head.data

	def peekLast(self):
		if self.isEmpty():
			raise RuntimeError("Empty List")
		return self.tail.data

	def removeFirstNode(self):
		if self.isEmpty():
			raise RuntimeError("Empty List")
		
		data = self.head.data 

		self.head = self.head.nextNode
		self.size -= 1

		if self.isEmpty():
			self.tail = None
		else:
			self.head.previousNode = None

		return data

	def removeLastNode(self):
		if self.isEmpty():
			raise RuntimeError("Empty List")

		data = self.tail.data
		self.tail = self.tail.previousNode
		self.size -= 1

		if self.isEmpty():
			self.head = None
		else:
			self.tail.nextNode = None
		return data
	
	def remove(self, node):
		if node.previousNode == None:
			return self.removeFirstNode()
		if node.nextNode == None:
			return self.removeLastNode()

		# make the pointers of adjacent nodes skip over selected removal node
		node.nextNode.previousNode = node.previousNode
		node.previousNode.extNode = node.nextNode

		data = node.data

		#memory cleanup
		node.data = None;
		node = node.previousNode = node.nextNode = None

		size -= 1

		return data
	


print("Init")
dll = DoubleLinkedList()
print("creating nodes")
dll.addFirst(1)
print(dll.peekFirst())
print("first node complete")
dll.addLast(27)
print(dll.peekLast())
print("second")
dll.addLast(30)
print(dll.peekLast())
print("thrid")
print("rmv 3")
print(dll.removeLastNode())
print("peekLast")
print(dll.peekLast())









		
