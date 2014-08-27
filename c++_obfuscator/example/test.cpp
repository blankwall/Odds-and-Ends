/* 
welcome to my program 




*/
#include "base64_.h"
#include <iostream>
using namespace std;
#define hello 100
#define hoopla(x) x*5
#define fastcopy(x,y,z) /*xyz*/ 
#define SWAP(a, b)  {                   \
                        a ^= b;         \
                        b ^= a;         \ 
                        a ^= b;         \
                    } 


/* This is a comment
fdkdsfksfdk
dsflflsdk
this tells all the code secrets
*/

// A class to represent pets.
class Pet {
public:

  // We want a constructor that initializes the pet's name.
  Pet(const string& s) : name(s) { }

  // Notice that we define "display" in Pet but don't in Cat.
  void display() const { cout << name << endl; }

protected:
  string name;
};

// Cats are Pets, at least for the purpose of our program.  To let C++
// know that, we put the " : public Pet" in between "class Cat" and the 
// curly brace.
class Cat : public Pet {
public:
  // The Cat constructor shown in the comment below didn't work. 
  // We got acompilation error
  // saying that there was no default constructor for the Pet 
  // class.  That was true, but we didn't try calling the
  // Pet default constructor.  At least not that we knew about.  But C++
  // tried to call it for us.  Where?  In the initialization list.  We
  // didn't write an initialization list!  C++ pretends that we
  // wrote "Cat (string s) : Pet() {".   If we want to avoid it, we
  // *have to* invoke some other Pet constructor in the intialization
  // list.
  // Cat (const string& s) { name = s; }

  // Here is a working version of the Cat constructor.  By calling the 
  // Pet constructor, it will initialize the cat's name.
  Cat (const string& s) : Pet(s) { }

  void meow() {}
};


int bone() ;

int print(int x){
	return x;
}

int main() {
  int x = print(5);
  const std::string s = "Here is some encoded data\n YAYAYYAYAYA!!!!!" ;

  for(; x > 0; --x){
  	cout << "Hey GONE!" << endl;
  }

  std::string encoded = base64_encode(reinterpret_cast<const unsigned char*>(s.c_str()), s.length());
  std::string decoded = base64_decode(encoded);

  /* this is also a comment */

  std::cout << "encoded: " << encoded << std::endl;
  std::cout << "decoded: " << decoded << std::endl;

  bone();


  Pet p("Felix");
  p.display();
  // If we try to make a pet "meow", then we will get a compilation error:
  //p.meow();

  Cat c("Heathcliffe");
  // We are using a member function that we never explicitly defined,
  // the "display" member function for a Cat.  Code reuse in action!
  c.display();
  // Cats can do something that other Pets cannot, the can meow.
  c.meow();
  return 0;
}

/*
  Example of addresses, pointers and pointer arithmetic.
  Also the use of pointers as array names.
  John Sterling
  CS1124
  Polytechnic University
*/


int bone() {

  int x = 6;
  int y = 5;
  SWAP(x,y);
  cout << "x = " << x << endl;
  // The address of x is writte &x
  cout << "&x = " << &x << endl;

  // declaring a pointer to an int and initializing it to  the address
  // of an int variable.  Note that pointers always have a type!
  int* px = &x;
  // Print out the contents of a pointer variable.
  cout << "px = " << px << endl;
  // Print out the value that the pointer points to.
  // When you use the * character on the left side of a pointer
  // variable it is called the "dereferencing operator".
  cout << "*px = " << *px << endl;

  int f[] = { 8, 13, 21, 34, 55, 89 };
  int* pf;
  // We will print out the contents of the array f[]
  cout << "f[] = { ";
  // Looping over an array using pointers.
  // Note that the name of an array is the array's address 
  for (pf = f; pf < f + 6; pf++) cout << *pf << ", "; 
  cout << "}\n";

  // Here is a second way of getting the address of an array.
  pf = &f[0];
  cout << "*pf = " << *pf << endl;
  // What is "*pf + 2" ?  In other words, which has higher precedence,
  // the dereferencing operator or the addition operator?
  cout << "*pf + 2 = " << *pf + 2 << endl;
  cout << "*(pf + 2) = " << *(pf + 2) << endl;
  // What is the effect of using dereferencing and pre-increment?
  cout << "*++pf = " << *++pf << endl;
  // What is the effect of using dereferencing and post-increment?
  cout << "*pf++ = " << *pf++ << endl;
  cout << "*(pf + 2) = " << *(pf + 2) << endl;
  // See that f has not changed, even though pf has.
  cout << "*(f + 2) = " << *(f + 2) << endl;
  cout << "f[2] = " << f[2] << endl;
  // Could we do the same with f as we did with pf above?
  // That is, can we use f++?  No.  VC++ complains that "++ needs and l-value".
  // That means we have to be able to assign to f.  But we can't write "f = 5"
  // or any other such assignment expression.  Another way to view it is that
  // f is const.  It may represent an address, but we can't change what that
  // address is.
  // f++;

  // If the name of an array is really just the address of the array
  // and if a pointer to the array holds the address of the array,
  // is there some easy way to use a pointer AS an array?  Yes!
  pf = f;
  cout << "pf[2] = " << pf[2] << endl;


  // What is the type of a and of b?
  int* a, b;

  // How do we define a pointer to a pointer?
  // See the use of two asterisks?  Note that we use an int** to hold the
  // address of an int*.
  int** pp = &px;
  cout << "**pp = " << **pp << endl;
  return 5;

}
