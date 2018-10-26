def convert2RPN(expression):
	length = len(expression)
	operationList = ['+', '-', '*', '/', '^']
	rightParen = ')'
	leftParen = '('

	operationList = {}
	operationList["^"] = 4
	operationList["*"] = 3
	operationList["/"] = 3
	operationList["+"] = 2
	operationList["-"] = 2
	operationList["("] = 1

	outList = []

	opStack = []

	for i in expression:

		# Left parenthesis
		if (i == leftParen):
			opStack.append(i)

		# Right parenthesis -> Pop until removing
		# the corresponding Left parenthesis. 
		# append the popped operators
		elif (i == rightParen):
			while (True):
				token = opStack[-1]

				if (token == leftParen):
					opStack.pop()
					break
				else:
					opStack.pop()
					if (token in operationList):
						outList.append(token)

		# Put the new operand in the list
		# First remove any operators that have higher or equal
		# precedence and append them to the output list
		elif (i in operationList.keys()):
			new_rank = operationList[i]

			index = 1

			while(True):
				key = opStack[-index]
				if (operationList[key] >= new_rank):
					outList.append(key)
					opStack.pop(-index)
					index = index + 1
				else:
					break
			
			# Then add the new operand to the stack
			opStack.append(i)

		# Operands -> Append it to the end of the output list
		else:
			outList.append(i)
	if (len(opStack) > 0):
		outList.append(opStack[::-1])
	return ''.join(outList)

def main():
	numOfLines = input()

	for i in range(int(numOfLines)):
		infixStr = input()
		print(convert2RPN(infixStr))

if __name__ == "__main__":
    main()