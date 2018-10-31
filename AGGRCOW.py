def bs(stallCoordinates, numOfCows):
	sortedStallCoordinates = sorted(stallCoordinates)

	lo = 0
	hi = (int)(1e10)

	while (lo < hi - 1):
		mid = (lo + hi) // 2

		# Min distance can be larger
		if (tryPutCows(mid, sortedStallCoordinates, numOfCows)):
			lo = mid

		# Min distance needs to be smaller
		else:
			hi = mid


	print(lo)



def tryPutCows(minDistance, sortedStallCoordinates, numOfCows):
	lastestCow = sortedStallCoordinates[0]
	cowCnt = 1

	for coord in sortedStallCoordinates:
		if (coord >= lastestCow + minDistance):
			cowCnt += 1
			lastestCow = coord


	if (cowCnt < numOfCows):
		return False
	else:
		return True


def main():
	numOfTests = input()

	for i in range(int(numOfTests)):
		(numOfStalls, numOfCows) = input().split(' ')

		stallCoordinates = []

		for i in range(int(numOfStalls)):
			coord = int(input())
			stallCoordinates.append(coord)

		bs(stallCoordinates, int(numOfCows))



if __name__ == "__main__":
    main()