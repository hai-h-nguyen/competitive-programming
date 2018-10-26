def convert2RPN(expression):
	length = len(expression)
	operationList = ['+', '-', '*', '/', '^']
	rightParen = ')'
	leftParen = '('

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
		elif (i in operationList):
			operation_rank = operationList.index(i)

			for index in range(1, len(opStack)):
				if (opStack[-index] in operationList):
					if (operationList.index(opStack[-index]) >= operation_rank):
						opStack.pop(-index)
						# Add this operand to the output list
						outList.append(opStack[-index])
			
			# Then add the new operand to the stack
			opStack.append(i)

		# Operands -> Append it to the end of the output list
		else:
			outList.append(i)

	outList.append(opStack[::-1])
	return outList

def main():
	numOfLines = input()

	for i in range(int(numOfLines)):
		infixStr = input()
		print(convert2RPN(infixStr))

if __name__ == "__main__":
    main()