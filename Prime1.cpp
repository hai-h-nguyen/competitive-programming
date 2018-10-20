// Peter wants to generate some prime numbers for his cryptosystem. 
// Help him! Your task is to generate all prime numbers between two given numbers! 

// Input
// The input begins with the number t of test cases in a single line (t<=10). 
// In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space. 

// Output
// For every test case print all prime numbers p such that m <= p <= n, one number per line, test cases separated by an empty line.

#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

bool checkPrime (int n)
{
	for (int dividend = 2; dividend < n; dividend++)
	{

		if (n % dividend == 0)
			return true;

		if (dividend * dividend >= n)
			break;
	}

	return false;

}

int main() {
	
	int NumberOfTests = 0;
	int upper, lower;
	cin >> NumberOfTests;

	// upper = 20;
	// lower = 10;
	// NumberOfTests = 2;

	while(NumberOfTests--)
	{
		//Read in in two integers and find all the primes between them. 
		cin >> lower >> upper;

		if (lower <= 2)
			lower = 2;

		for(int i = lower; i <= upper; i++)
			if(checkPrime (i) == false)
				cout << i << endl;
	}
	return 0;
}