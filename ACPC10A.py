"""Input

Your program will be tested on one or more test cases. 
Each case is specified on a single line with three integers (−10, 000 < a1 , a2 , a3 < 10, 000) where a1 , a2 , and a3 are distinct.
The last case is followed by a line with three zeros.
Output

For each test case, you program must print a single line of the form:
XX v
where XX is either AP or GP depending if the given progression is an Arithmetic or Geometric Progression. v is the next 
member of the given sequence. All input cases are guaranteed to be either an arithmetic or geometric progressions.
"""

def check(num1, num2, num3):
	
	if (num1 + num3 == 2*num2):
		return ("AP", num3 + num2 - num1)

	if (num1 * num3 == num2 * num2):
		return ("GP", num3 * (num2 / num1))

def main():
	while(True):	
		(num1, num2, num3) = input().split(' ')

		(num1, num2, num3) = (int(num1), int(num2), int(num3))

		if ((num1 == 0) and (num2 == 0) and (num3 == 0)):
			break

		(result, next_element) = check(num1, num2, num3)

		print('%s %s' % (result, str((int)(next_element))))

if __name__ == "__main__":
    main()