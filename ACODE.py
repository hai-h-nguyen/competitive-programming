def recursiveFcn(inStr):
	n = len(inStr)

	if (n == 1):
		return (int(inStr) != 0)

	elif (n == 2):
		if (inStr[0]  == '0'):
			return 0

		if (inStr[1]  == '0'):
			return (int(inStr[0])  <= 2)

		return (1 + (int(inStr[0:2]) <= 26))

	else:
		return (inStr[0] != '0') * (recursiveFcn(inStr[1:]) + (int(inStr[0:2]) <= 26) * recursiveFcn(inStr[2:]))

def dpAlphaCode(inStr):
	List = []
	result = 0

	n = len(inStr)

	if (n <= 3):
		return print(int(recursiveFcn(inStr)))

	# Use dynamic programming with longer string
	# L[0]
	List.append(recursiveFcn(inStr[-1]))

	# L[1]
	List.append(recursiveFcn(inStr[-2:]))


	for i in range (3, len(inStr) + 1):
		tempStr = inStr[-i:]
		List.append((tempStr[0] != '0') * (List[i - 2] + (int(tempStr[0:2]) <= 26) * List[i - 3]))


	print(int(List[-1]))

def main():
	while (True):
		inStr = input()

		if (inStr == '0'):
			break
		else:
			dpAlphaCode(inStr)

if __name__ == "__main__":
    main()