def maxCard(fMaxCardLen):
	currentLen = 0
	n = 2

	while (currentLen < fMaxCardLen):
		currentLen += 1/n
		n = n + 1

	return str(n - 2)


def main():

	while (True):
		fMaxCardLen = float(input())

		if (fMaxCardLen == 0.0):
			break

		print(maxCard(fMaxCardLen) + " card(s)")

if __name__ == "__main__":
    main()