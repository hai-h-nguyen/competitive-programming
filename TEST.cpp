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

int main() {
	
	int inNumber = 0;
	int output[10000];
	const int STOP = 42;
	int startIdx = 0;

	while(true)
	{
		cin >> inNumber;

		if (inNumber == 42)
			break;

		output[startIdx++] = inNumber;

	}

	for (int i = 0; i < startIdx; i++)
	{
		cout << output[i] << endl;
	}

	return 0;
}