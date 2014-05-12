import sys
import os
import time
import subprocess as sub

x86 = []

ea = ScreenEA()
seg_ea = ea
print "STARTING AT: ", hex(ea)
#CURRENTLY HARD CODED 
end = 0x08048529
print "GATHERING CONSTRAINTS: "
for head in Heads(seg_ea, end):
# If it's an instruction
	if isCode(GetFlags(head)):
# Get the mnemonic 
		mnem = GetDisasm(head)
		if mnem != "nop":
			x86.append(mnem)
		

output = file("/home/blankwall/Desktop/lopo", "wb")
#write output to file
for i in x86:
	output.write(i + "\n")
print "SOLVING"
#call solver   CHANGE TO PROPER DIRECTORY
a = sub.Popen("/home/blankwall/Desktop/loopManip.py", stdout = sub.PIPE )
#wait for solver to finish
a.wait()
#print solvers result
print file("/home/blankwall/Desktop/polo").read()



