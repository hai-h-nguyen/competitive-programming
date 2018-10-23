"""A positive integer is called a palindrome if its representation in the decimal system is the same when read from 
left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the
value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.
Input

The first line contains integer t, the number of test cases. Integers K are given in the next t lines.
Output

For each K, output the smallest palindrome larger than K.
"""

def isPalindrome(numInt):
    tempList = []

    while (numInt > 0):     
        tempList.append(numInt % 10)
        numInt //= 10

    L = len(tempList)
    for i in range(0, L//2):
        if (tempList[i] != tempList[L - 1 - i]):
            return False

    return True

def main():
	numOfTests = input()

	for i in range(int(numOfTests)):
		numInt = int(input())

		while (True):
			numInt += 1
			if (isPalindrome(numInt) == True):
				break

		print(numInt)

if __name__ == "__main__":
    main()