def factorial(n):
	result = 1


	for i in range(1,n + 1):
		result *= i


	return result

def main():
	numOfLines = input()

	for i in range(int(numOfLines)):
		num = input()
		print(factorial(int(num)))

if __name__ == "__main__":
    main()