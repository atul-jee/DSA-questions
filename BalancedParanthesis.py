def isBalanced(string):
	s=[]

	for ele in string:
		if ele in '({[':
			s.append(ele)
		elif ele==')':
			if not s or s[-1]!='(':
				return False
			s.pop()
		elif ele == '}':
			if not s or s[-1]!='{':
				return False
			s.pop()
		elif ele == ']':
			if not s or s[-1]!='[':
				return False
			s.pop()
	if not s:
		return True
	return False

def main():
	s=input()
	print(isBalanced(s))
if __name__ == '__main__':
	main()