// Input

// An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.
// Output

// For each integer n given at input, display a line with the value of n!

#include <iostream>
using namespace std;



long long factorial (long long n)
{
	long long i = 1;
	long long result = 1;

	for (i = 1; i <= n; i++)
	{
		result *= i;
	}

	return result;
}


int main() {
	
	// your code here
	int numOfLines = 0;
	int num = 0;

	cin >> numOfLines;

	while(numOfLines--)
	{
		cin >> num;
		if (n <= 20)
			cout << factorial(num) << endl;
		else
			
	}

	return 0;
}