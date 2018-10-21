

def checkStop(numInt):
	while (numInt % 2 == 0):
		numInt /= 2

	if (numInt == 1):
		return 'TAK'
	else:
		return 'NIE'

def main():
	numInt = input()
	numInt = int(numInt)

	print(checkStop(numInt))

if __name__ == "__main__":
    main()