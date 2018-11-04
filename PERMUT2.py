"""Input Specification

The input contains several test cases.
The first line of each test case contains an integer n (1 ≤ n ≤ 100000). Then a permutation of the integers 1 to n follows in the next line.
There is exactly one space character between consecutive integers. You can assume that every integer between 1 and n appears exactly once in 
the permutation.
The last test case is followed by a zero.
Output Specification

For each test case output whether the permutation is ambiguous or not. Adhere to the format shown in the sample output. 
"""

def isAmbiguous(arrayIn, arraySize):
    myDict = {}
    arrayOut = []

    for num in arrayIn:
        myDict[num] = arrayIn.index(num) + 1

    for key in sorted(myDict.keys()):
        arrayOut.append(str(myDict[key]))

    check = (arrayIn == arrayOut)
    if (check):
        print('ambiguous')
    else:
        print('not ambiguous')

def main():

    while(True):
        arraySize = int(input())

        if (arraySize == 0):
            break

        array = []
        array = input().split()

        isAmbiguous(array, arraySize)

if __name__ == "__main__":
    main()