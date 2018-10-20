// Number of trailing zeros in n!

#include <iostream>
using namespace std;



int test(int M)

{
	int count = 0;

	while (M % 5 == 0)
	{
		M = M/5;
		count++;
	}

	return count;

	// cout << count;
}

int numOfZeros (int n)
{
	int M = 0;

	if (n == 1)
		return 0;
	else
	{
		return numOfZeros (n - 1) + test(n);
	}
}


int main() {
	
	// your code here
	int num = 0;

	cin >> num;

	// test(num);

	cout << numOfZeros(num);

	return 0;
}