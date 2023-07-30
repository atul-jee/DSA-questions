class Stack:
	def __init__(self):
		self.data=[]
		self.count=0
	def push(self,item):
		self.data.append(item)
		self.count=self.count+1
	def pop(self):
		if self.isEmpty():
			print("Can't be pop, Stack is Empty!")
			return None
		else:
			self.count=self.count-1
			return self.data.pop()
			
	def isEmpty(self):
		return self.count==0
	def size(self):
		return self.count
	def top(self):
		if self.isEmpty():
			print("Stack is Empty!!!")
			return None
		return self.data[-1]


		