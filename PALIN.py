"""A positive integer is called a palindrome if its representation in the decimal system is the same when read from 
left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the
value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.
Input

The first line contains integer t, the number of test cases. Integers K are given in the next t lines.
Output

For each K, output the smallest palindrome larger than K.
"""

def nextPalindrome(numStr):

    length = len(numStr)
    nextPalin = ''

    if (length % 2 == 0):

        half_index = length // 2
        half_str = numStr[:half_index]

        nextPalin = half_str + half_str[::-1]

        if (nextPalin <= numStr):
            half_str = str(int(half_str) + 1)
            nextPalin = half_str + half_str[::-1]

    else:
        half_index = length // 2
        half_str = numStr[0 : half_index]

        nextPalin = half_str + numStr[half_index] + half_str[::-1]

        if (nextPalin <= numStr):
            half_str = str(int(half_str + numStr[half_index]) + 1)
            nextPalin = half_str + half_str[0:half_index][::-1]

    return nextPalin


def main():
    numOfTests = input()

    for i in range(int(numOfTests)):
        numStr = input()

        check = True
        for i in numStr:

            # Special treat for "9...9" input
            if (i != '9'):
                check = False

        if (check):
            numStr = str(int(numStr) + 1)
        
        print(nextPalindrome(numStr))

if __name__ == "__main__":
    main()