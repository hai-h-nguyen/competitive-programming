// Number of trailing zeros in n!

#include <iostream>
using namespace std;


int main() {
	
	int dimension = 1;


	while(true)
	{
		cin >> dimension;

		if (dimension != 0)
			cout << dimension * (dimension + 1) * (2 * dimension + 1)/6 << endl;
		else
			break;
	}

	return 0;
}