#include <iostream> // preprocesser directive, tells the computer that you will be using a file, essantialy an import statment but unlike using namespace which imports a library 
// include imports a file

using namespace std; // using namespace imports a library like include but it imports a LIBRARY not a FILE
// std stands for standard cpp LIBRARY

// every program has a main function
int cpptoutorial()
{
    //cout  = output stream object
    //<<  = streem insertion operator
    cout << "Hello World!" << endl;

    //examples of cout
    cout << "I lke bacon" << endl;
    //endl means that it ends the line and starts a new one 
    cout << "And Ham" << endl;

    //return = returns a value
    //return 0 = no errors
    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu
