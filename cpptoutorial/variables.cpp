#include <iostream>

using namespace std;

int main() 
{
	// int type use java init syntax
	int x = 10;
	int a;
	int b;
	int sum;

	// << = write out operator
	// >> = writ in oprator
	cout << "Enter a number: "<< endl;
	// writes input to varuble a 
	cin >> a;
	// int a = input;


	cout << "Enter a nother number: "<< endl;

	cin >> b;

	sum = a + b;
	cout << "The sum of " << a << " + " << b << " is " << sum;
	return 0;
}