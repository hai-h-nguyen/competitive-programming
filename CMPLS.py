def print_array(array):
	for el in array:
		print(el, end = ' ')

	print("")

def str_to_list(string): 
    li = list(string.split(" ")) 
    li = [int(el) for el in li]
    return li 	

def cmpls(list_in, num_of_numbers):

	list_len = len(list_in)

	if (list_len == 1):
		result = []
		for i in range(num_of_numbers + 1):
			result.append(list_in[0])
		result = result[-num_of_numbers:]
		return result

	D_list = []
	D_list.append(list_in)
	start = 1
	check_cnt = 0

	current_list = list_in

	while(True):
		# Calculate D_x(n)
		# print("Pre", D_list)
		temp = [current_list[i + 1] - current_list[i] for i in range(len(current_list) - 1)]
		D_list.append(temp)
		# print("After", D_list)

		# Check if all elements in this list is the same
		for elem in D_list[start]:
			if elem != D_list[start][0]:
				check_cnt = 0
				break
			else:
				check_cnt += 1

		# Now we back compute 
		if (check_cnt == len(D_list[start])):
			# print("Final", D_list)
			total_len = len(list_in) + num_of_numbers

			current_list = D_list[-1]
			for i in range(len(current_list), total_len):
				current_list.append(current_list[0])
			D_list[-1] = current_list

			# print("Debug", D_list, len(D_list))


			for i in range(len(D_list) - 1, -1, -1):
				# print(i)

				current_D_len = len(D_list[i])
				for j in range(current_D_len, total_len):
					temp = D_list[i][j-1] + D_list[i+1][j-1]
					D_list[i].append(temp)

			return D_list[0][-num_of_numbers:]

		# Go to the next round to compute D
		else:
			current_list = D_list[start]
			start += 1




def main():

	num_of_test = int(input())

	for i in range(num_of_test):
		first_line = input()
		first_list = str_to_list(first_line)
		C = first_list[0]
		S = first_list[1]

		second_line = input()
		list_in = str_to_list(second_line)
		result = cmpls(list_in, S)
		print_array(result)

if __name__ == "__main__":
    main()