def calculate_squared_digit(num_in):
	total = 0
	while(True):
		temp = num_in % 10
		total += temp * temp
		num_in = (num_in - temp) // 10

		if (num_in == 0):
			break
	return total


def main():
	num_2_test = int(input())
	count = 0

	listTemp = []

	while(True):
		temp = calculate_squared_digit(num_2_test)
		num_2_test = temp
		count += 1

		if (temp == 1):
			print(count)
			return

		if (temp not in listTemp):
			listTemp.append(temp)
		else:
			print("-1")
			return

if __name__ == "__main__":
    main()