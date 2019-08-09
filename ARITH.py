def simpleArith(num_1, num_2, operand):
	str_1 = str(num_1)
	str_2 = str(num_2)
	len_2 = len(str_2) + 1
	len_1 = len(str_1)

	space = max(len_2, len_1)


	if (operand == '-' or operand == '+'):

		print(str_1.rjust(space, ' '))
		string = operand + str_2
		print(string.rjust(space, ' '))
		# print('-'*space, end = '')

		if (operand == '-'):
			result = num_1 - num_2
		else:
			result = num_1 + num_2
		
		result_str = str(result)
		result_len = len(result_str)

		result_len_1 = max(len_2, result_len)

		dash_2 = '-'*result_len_1

		space = max(space, result_len_1)
		print(dash_2.rjust(space, ' '))
		print(result_str.rjust(space, ' '))
	
	else:

		result = num_1 * num_2
		result_str = str(result)
		result_len = len(result_str)

		if (num_2 < 10):
			space = max(space, result_len)
			print(str_1.rjust(space, ' '))

			string = operand + str_2
			print(string.rjust(space, ' '))
			
			print('-'*space, end = '')		
			print('\n' + str(result).rjust(space, ' '))

			return


		space = max(space, result_len)
		
		# Print num_1
		print(str_1.rjust(space, ' '))

		# Print operand + num_2
		string = operand + str_2
		print(string.rjust(space, ' '))

		# Print dash line
		temp_result = num_1 * int(str_2[-1])
		dash_1_cnt = max(len_2, len(str(temp_result)))

		dash_1 = '-'*dash_1_cnt
		print(dash_1.rjust(space, ' '))


		for i in range(1, len_2):
			temp_result = num_1 * int(str_2[-i])
			result_str = str(temp_result)
			result_str = result_str + ' '*(i-1)

			print(result_str.rjust(space, ' '))
	
		dash_2 = '-'*result_len
		print(dash_2.rjust(space, ' '))
		print(str(result).rjust(space, ' '))

def main():
	numOfTests = int(input())

	for i in range(int(numOfTests)):
		numStr = input()
		if ('+' in numStr):
			numStr = numStr.split('+')
			simpleArith(int(numStr[0]), int(numStr[1]), '+')
		elif ('-' in numStr):
			numStr = numStr.split('-')
			simpleArith(int(numStr[0]), int(numStr[1]), '-')		
		else:
			numStr = numStr.split('*')
			simpleArith(int(numStr[0]), int(numStr[1]), '*')				
if __name__ == "__main__":
    main()