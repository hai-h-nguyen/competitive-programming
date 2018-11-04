// Input Specification

// The input contains several test cases.
// The first line of each test case contains an integer n (1 ≤ n ≤ 100000). Then a permutation of the integers 1 to n follows in the next line.
// There is exactly one space character between consecutive integers. You can assume that every integer between 1 and n appears exactly once in 
// the permutation.
// The last test case is followed by a zero.
// Output Specification

// For each test case output whether the permutation is ambiguous or not. Adhere to the format shown in the sample output. 


#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int find(int arr[], int len, int seek)
{
    for (int i = 0; i < len; ++i)
    {
        if (arr[i] == seek) return i;
    }
    return -1;
}


void isAmbiguous(int arr_in[], int size)
{
	int output_arr[size];

    for (int i = 0; i < size; i ++)
    {
    	output_arr[arr_in[i] - 1] = i + 1;
    }

    bool isAmb = true;

    for (int i = 0; i < size; i ++)
    {
        if (output_arr[i] != arr_in[i])
        {
        	isAmb = false;
        	break;
        }
    }

    if (isAmb)
    	cout << "ambiguous" << endl;
    else
    	cout << "not ambiguous" << endl;
}

int main() {
	
	int n = 0;

	while(true)
	{
		cin >> n;

		if (n == 0)
			break;

		int input_arr[n];

		for (int i = 0; i < n; i++)
		{
			cin  >> input_arr[i];
		}

		isAmbiguous(input_arr, n);
	}

	return 0;
}