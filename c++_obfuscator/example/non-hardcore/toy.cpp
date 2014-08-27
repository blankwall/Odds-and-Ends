/*
	Example of an array of objects. 
	John Sterling
	CS1124
	Polytechnic University
*/

#include <iostream>
using namespace std;

class Foo {
public:
	Foo() {
	cout << "In Foo's default constructor, Foo()\n";
	}
	void setX(int xValue) {
		fooby = xValue;
	}
	void display() const {
		cout << "x = " << fooby << endl;
	}
	
private:
	int fooby;
};


// The code below demonstrates 
//   1) the creation of an array of objects.  
//		Note that the default constructor is called for every object in the array.
//   2) For each object in the array, calling a function, "setX", 
//		that takes an argument.
//   3) For each object in the array, calling a function, "display", 
//		that does not take an argument.
// Note the use of the "dot operator" in expressions like "arr[i].display()"
int main() {
	cout << "Creating a single Foo:\n";
	Foo x;
	cout << "Creating an array of five Foo's:\n";
	Foo arr[5];
	cout << "Setting the x value of object arr[i] to i*i for all five Foo's\n";
	for (int i = 0; i < 5; i++)
		arr[i].setX(i * i);
	for (int i = 0; i < 5; i++) {
		cout << "Displaying arr[" << i << "]\n";
		arr[i].display();
	}
}
