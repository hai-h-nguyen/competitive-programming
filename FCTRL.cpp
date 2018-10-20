// Number of trailing zeros in n!

#include <iostream>
using namespace std;



int numOfZerosInFactorial (int n)
{
	int a = 0;
	int numOfZeros = 0;

	while (n >= 5)
	{
		n = n / 5;
		numOfZeros += n;
	}

	return numOfZeros;
}


int main() {
	
	// your code here
	int numOfTest = 0;
	int num = 0;
	int a = 0;

	cin >> numOfTest;

	while(numOfTest--)
	{
		cin >> num;
		cout << numOfZerosInFactorial(num) << endl;
	}

	return 0;
}