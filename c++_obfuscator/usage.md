#USAGE

The program relies on two things first is the configuration file and second is command line arguments

#Configuration 

All that has to be in here is your function names and variable names that need to be replaced.

# Command Line

All files to be parsed by the program are passed in via the command line. All h and cpp files relying on each other should be passed in the same run to ensure there functions are renamed properly.  

**Note there is a python list called types at the top of the program. Add C++ types here to have them put into the define list. ie string char int etc...**



##Coding guidelines to make the obfuscator more effective:

1 Dont use variable names that include type names ie. int int_one = 5; 
	*Obfuscator will pick up both ints and change them messing up your program
	
2 Dont use single character variables two characters is usually fine. ie int i = 0; should be int count = 0;

3 Put defines after using declaration and add names to the config file ie.
	*using namespace std;
	*#define hello 100
	*#define hoopla(x) x*5



