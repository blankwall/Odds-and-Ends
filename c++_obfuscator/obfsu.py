from random import randint
import random
import string
import os.path
import sys

#defines how long defines are need to add dictionary words instead
random_length = 5
#defines max number of spaces 
space_length = 20
#defines amount of times to dereference the define list
deref = 20

var_length = 0

syntax = [";", '"',")", "(", " ", ".", "{", "}", "<", ">", ":", "[", "*", "&", "+", ","]

#Add types here as needed
types = ["int", "class","public", "protected","bool", "static", "void", "const", "unsigned", "<<", "cout", "endl", "return", "while", "if", "for", "else", "length", "c_str","reinterpret_cast"]


class file_:
	def __init__(self):
		self.funcs_ = {}
		self.types = {}
		if os.path.isfile("config.ini"):
			y = file("config.ini").readlines()
			for k in y:
				k = k.strip()
				self.funcs_[k] = id_generator(random_length)


#Change to a dicitionary list rather then ranom characters to make visual analysis harder
def ran_char():
	#x = randint(0x41, 0x5a);
	return ""#chr(x)

def id_generator(size):
	global var_length
	var_length += 1
	#chars = string.ascii_uppercase + string.digits
	return "_" * var_length #ran_char() + ''.join(random.choice(chars) for _ in range(size-1))


#convert stander quotes string to hex representation
def hex_string(x):
	x = x.replace("\\n", "\n")
	x = x.encode('hex')
	final_Str = ""
	y = "\\x"
	for i in range(0, len(x), 2):
		v = y
		v += x[i:i+2]
		final_Str += v
	return '"' + final_Str + '"'

#change numbers ie  5 to 0xf3a-0xf35
def fuck_num(x):
	if(x == 0):
		base  = randint(0, 0xffffff/2)
		base2 = randint(0, 0xffffff/2)
		return "((" + hex(base) + " + " +hex(base2) + ") - (" + hex(base) + " + " + hex(base2) +  "))"
	else:
		base = randint(0,0x7fffffff)
		base /= x
		newb = (base+x)
		equate = "(" + hex(newb) + " - " + hex(base) + ")"
		return equate 

#get the quoted part of a string simple line parser 
def replace_string(i):
	count = quote = end = start = 0
	for k in i:
		if k == '"':
			if start != 0:
				end = count + 1
				quote += 1
				break
			start = count
			quote += 1
		count += 1
	if quote == 2:
		newb = hex_string(i[start:end].replace("\"", "").strip())
		i = list(i)
		i[start:end] = newb
	return "".join(i)

#Safe replace ensure your not replacing things in the middle of words 
def safe_replace(line, replace,x, function):
	word = line.find(replace)
	front = back = ""
	if word != 0:
		front = line[word-1]

	if (word +len(replace)) < len(line):
		back = line[word+len(replace)]

	if front in syntax or front == " " or front == "":
		if back in syntax or back == " " or back == "":
			if function == "func":
				line = line.replace(replace, x.funcs_[replace])
			elif function == "type":
				line = line.replace(replace, x.types[replace])
	return line

# Creating defines needed from the types at the top of the file
def defines(x):
	reter = ""
	new_type = {}
	finals = []
	count = 0
	for i in types:
		reter += "#define "
		temp = ran_char() + id_generator(randint(random_length,random_length))
		x.types[i] = temp
		reter += str(temp) + " " + i +"\n"
	return reter

#add multiple layers of dereference to make it harder to parse the define tree
def deref_(x):
	reter = ""
	new_type = {}
	random.shuffle(types)
	for i in types:
		tempor = ran_char() + id_generator(randint(random_length,random_length))
		new_type[x.types[i]] = tempor
		reter += "#define "
		reter += str(new_type[x.types[i]]) + " " + x.types[i] +"\n"
		x.types[i] = new_type[x.types[i]]
		#maybe put extra defines here
	return reter

#changing spacing to make it difficult to understand
def change_space(i):
	x_ = randint(1,18)
	x_ = " " * x_
	i = i.replace(" ", x_)
	return i

# #Safe replace ensure your not replacing things in the middle of words 
# # FIX THIS TO HANDLE MORE THEN ONE NUMBER IN A LINE
# def safe_number(line):
# 	nums = []
# 	front =  0
# 	for count in range(0, len(line)):
# 		num = ""
# 		if line[count].isdigit():
# 			front = count
# 			if line[count-1] not in syntax:
# 				continue
# 			num += line[count]
# 			count += 1
# 			try:
# 				while line[count].isdigit() and (count < len(line)-2):
# 					num += line[count]
# 					count += 1
# 			except:
# 				return line
# 			print front, count
# 			line = list(line)
# 			line[front:count] = str(fuck_num(int(num)))
# 			line = "".join(line)
# 			break
		
# 	return line

def parse_code(code, d,x):
	final = ""
	value = defined = comment = 0
	skip = ["#include", "using"]

	for i in range(0, len(code)):
		i = code[i].strip()

		#comment skipping
		if i[0:2] == "//":
			continue

		#comment skipping
		if "/*" in i:
			comment = 1

		if comment == 1:
			if "*/" in i:
				comment = 0
				continue
			else:
				continue

		#pass over includes
		if len(i) > 0 and i[0] == '#' and not value:
			final += i
			final += '\n'
			continue
		else:
			value = 1

		if value == 1 and defined == 0:
			i += "\n"
			final += i
			final += defines(x)
			for kooopa in range(deref):
				final += deref_(x)

			defined = 50
			continue

		pass_ = 0
		for passed in skip:
			if passed in  i:
				final += i
				final += "\n"
				pass_ = 1
		if pass_:
			continue

		i = replace_string(i)

		#FIX THIS
		# i = safe_number(i)
		for function in x.funcs_:
			if function in i:
				i = safe_replace(i, function, x, "func")

		for type_ in x.types:
			if type_ in i:
				i = safe_replace(i, type_, x, "type")

		i = change_space(i)
		final += i
		final += "\n"

	d.write(final)



def main():
	x = file_()
	count =0
	for i in sys.argv:
		if count == 0:
			count += 1
			continue
		fil_ = i
		code = file(fil_).readlines()
		fil_ = fil_.split(".")
		fil_[0] += "_."
		fil_ = "".join(fil_)
		print "CREATING: " + fil_
		d = file( fil_ , "w")
		parse_code(code,d,x)





main()

