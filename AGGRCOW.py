def bs(stallCoordinates, numOfCows):
	stallCoordinates = sorted(stallCoordinates)

	lo = stallCoordinates[0]
	hi = stallCoordinates[-1]

	while (low < hi - 1):
		mid = (low + hi) // 2


def tryPutCows(minDistance, sortedStallCoordinates, numOfCows):
	firstCow = sortedStallCoordinates[0]

	maxCows = (sortedStallCoordinates[-1] - firstCow) // minDistance

	if (maxCows > numOfCows):
		return false
	else:
		return true


def main():
	numOfTests = input()

	for i in range(int(numOfTests)):
		(numOfStalls, numOfCows) = input().split(' ')

		stallCoordinates = []

		for i in range(int(numOfStalls)):
			stallCoordinates.append(int(intput()))



if __name__ == "__main__":
    main()