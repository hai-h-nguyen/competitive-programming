def lastDigit(base, index):
	r = base % 10
	if (index <= 4):
		return ((r ** index) % 10) 	
	if (r == 2):   return (6 * lastDigit(2, index % 4) % 10)
	elif (r == 4): return lastDigit(2, 2*index)
	elif (r == 8): return lastDigit(2, 3*index)
	elif (r == 3): return lastDigit(3, index % 4)
	elif (r == 7): return lastDigit(7, index % 4)
	elif (r == 9): return lastDigit(3, 2*index)
	else: return r
def main():
	numOfLines = input()
	for i in range(int(numOfLines)):
		(base, index) = input().split(' ')
		(base, index) = (int(base), int(index))
		finalDigit = lastDigit(base, index)
		print(finalDigit)
if __name__ == "__main__":
    main()