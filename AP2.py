"""
Input

First line will contain a number indicating the number of test cases.

Each of the following t lines will have 3 number '3term' ,'3Lastterm' and 'sum'

3term  - is the 3rd term in of the series and

3Lastterm  - is the 3rd term in of the series and

sum - is the sum of the series.
Output

For each input of the test case, you need to print 2 lines.

First line should have 1 value - the number of terms in the series.

2nd line of the output should print the series numbers separated by single space.
"""
def main():
    numOfTests = input()
    List = []

    for i in range(int(numOfTests)):
        (third_term, third_Lastterm, Sum) = input().split(' ')

        third_Lastterm = int(third_Lastterm)
        third_term = int(third_term)
        Sum = int(Sum)

        checkN = (2 * Sum) % (third_term + third_Lastterm)
        n = (2 * Sum) // (third_term + third_Lastterm) - int(checkN)
        
        T = (third_Lastterm - third_term) / (n - 5)
        a0 = third_term - 2*T

        print(n)
        for i in range(1, n + 1):
            print((int)(a0 + (i - 1) * T), end = ' ')

        print('')      

if __name__ == "__main__":
    main()