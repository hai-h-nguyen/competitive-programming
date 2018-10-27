def nextCubeEnd888(ith):
	return 192 + (ith - 1) * 250

def main():
	numOfTests = input()

	for i in range(int(numOfTests)):
		ith = int(input())
		print(nextCubeEnd888(ith))

if __name__ == "__main__":
    main()