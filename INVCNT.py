def countInversion(arrIn):
	inversionCnt = 0

	while(True):
		n = len(arrIn)

		if (n == 1):
			break

		indexOfMax = n - arrIn.index(max(arrIn[::-1])) - 1
		inversionCnt += len(arrIn) - indexOfMax - 1

		del arrIn[indexOfMax]

	print(inversionCnt)

def main():

	numOfTests = int(input())
	input()

	for i in range(numOfTests + 1):

		if (i >= 1):
			input()

		numOfElement = int(input())

		arrIn = []

		for cnt in range(numOfElement):
			temp = input()

			if (temp != ' '):
				arrIn.append(int(temp))

		countInversion(arrIn)

if __name__ == "__main__":
    main()