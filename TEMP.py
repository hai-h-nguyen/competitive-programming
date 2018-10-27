def Temp(inStr):
	n = len(inStr)

	if (n == 1):
		if (int(inStr) != 0):
			return 1
		else:
			return 0

	elif (n == 2):
		if (inStr[0]  == '0'):
			return 0

		if (inStr[1]  == '0'):
			if (inStr[0]  == '1'):
				return 1
			else:
				return 0


		if (int(inStr[0:2]) <= 26):
			return 2
		else:
			return 1

	else:
		if (int(inStr[0:2]) <= 26):
			a = Temp(inStr[1:])
			b = Temp(inStr[2:])

			if (a*b != 0):
				return (a + b)
			else:
				return 0
		else:
			return Temp(inStr[1:])

def main():
	while (True):
		inStr = input()

		if (inStr == '0'):
			break
		else:
			print(Temp(inStr))

if __name__ == "__main__":
    main()