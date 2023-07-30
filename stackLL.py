from Node import Node
class Stack:
	def __init__(self):
		self.top=None
		self.size=0

	def push(self,data):
		new_node=Node(data)
		new_node.next=self.top
		self.top=new_node
		self.size=self.size+1

	def pop(self):
		if self.isEmpty():
			print("Stack is Empty")
			return None
		pop_item=self.top.data
		self.top=self.top.next
		self.size-=1
		return pop_item

	def isEmpty(self):
		return self.top is None

	def size(self):
		return self.size

	def top(self):

		if self.isEmpty():
			print("Stack is Empty!!!")
			return None 
		return self.top.data



