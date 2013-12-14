import subprocess
import itertools

# Random number generator using itertools python
# Links with ki.c to call c file add comments update soon
#Thanks to Ki for helping write this

# This part writes a file and pushes it into gdb
tpl = """
file crackme
b * 0x80488c0
commands
	silent
	call/x 0x8048ea0("{0}")
	q
end
r
"""
#Turn string into hex
def hexify(x):
	return ''.join(r'\x%02x' % ord(i) for i in x)

#generator of strings
def gen_str():
	lst = []
	for i in range (65, 123):
		lst.append(chr(i))

	for i in range(10):
		for K in itertools.product(lst, repeat=i):
			yield "".join(K)
	# return ['a', 'b']

x = 0
for i in gen_str():

	#Call c funstion and catch output
	ret = subprocess.check_output(
		['/home/blankwall/Desktop/ki', i]
	)

	x += 1

	if x % 10000 == 0:
		print x
		print i

	#Compare output
	if int('0xef2e3558',16) == int(str(ret), 16): #0xef2e3558
		print "WINNER", i
		exit()

