// TEST - Life, the Universe, and Everything
// #basic #tutorial #ad-hoc-1

// Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. 
// More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42. 
// All numbers at input are integers of one or two digits.
// Input:
// 1
// 2
// 88
// 42
// 99


// Output:
// 1
// 2
// 88

#include <iostream>
using namespace std;

bool isPalindrome(long long numInt){
    long long tempList[1000000];
    long long lenCnt = 0;

    while (numInt > 0) {     
        tempList[lenCnt] = numInt % 10;
        numInt /= 10;
        lenCnt++;
    }

    for (int i = 0; i < lenCnt; i++)
    {
        if (tempList[i] != tempList[lenCnt - 1 - i])
            return false;
    }

    return true;
}

int main() {
	
	int numInt = 0;
	int numOfTests = 0;

	cin >> numOfTests;

	isPalindrome(numOfTests);

	while(numOfTests--)
	{
		cin >> numInt;

		while (true){
			numInt += 1;
			if (isPalindrome(numInt) == true)
			{
				break;
			}
		cout << numInt + 1 << endl;

		}

	}

	return 0;
}