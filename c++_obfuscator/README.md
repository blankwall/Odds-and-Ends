C++ Obfuscator
======

## Design Goals

The main objective of this program is to strip out valuable information from a program such as comments function names and variable names. Much of a programs logic can be derived simply from these valuable pieces of information. C++ is famous for being one of the few modern languages not relying on a context free grammar and is thus very difficult to parse. To combat this I rely upon the user to define which variables and functions to replace. 

## Other fun things

Yes parsing the define tree is easy and is not really obfuscation in its own right. But parsing the define tree 20 times is something most will write a script to do and thus waste valuable minutes they could be analyzing our code. Along the same lines is the spacing of  the program. It is very easy to fix the spacing but with variable amount of spaces throughout it will take more then a simple find replace thus wasting a bit more time. There is more to be added in the coming days so check the TODO list for more info on what is planned.

Finally check the usage file for a general overview of how to use the program as well as coding practices to make the program more effective. 
