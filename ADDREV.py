def reverse(n):
	n = str(n)


	n = n[::-1]

	return int(n)


def main():
	numOfLines = input()

	for i in range(int(numOfLines)):
		(num1, num2) = input().split(' ')

		num1 = reverse(num1)
		num2 = reverse(num2)

		num = num1 + num2
		num = reverse(num)

		print(num)

if __name__ == "__main__":
    main()