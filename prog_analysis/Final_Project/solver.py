#!/usr/bin/python
import re
from z3 import *
x86 = []
loops = []
debug = True
a = {}
count = ""

def prePass():
	loops = []
	out = []
	reg = None
	i = 0
	num = 0
	while(i < len(x86)):
		if x86[i][0] == 'jmp':
			out.append(x86[i])
			i += 1
			k = i
			while(x86[k][0] != "cmp"):
				reg = True
				out.append(x86[k])
				k += 1
				if (k >= len(x86)-1):
					break
			if x86[k][0] == "cmp":
				print "HERE", x86[k][2]
				if x86[k][2].isdigit():
					count = x86[k][2]
			i = k+1	
			if count:
				out = out*(int(count)+1)
			for l in out:
				loops.append(l)	
			
		loops.append(x86[i])
		i += 1

	if debug:
		for i in loops:
			print i
	return loops

def parseReg(reg):
	if reg.isdigit():
		return
	elif reg not in a:
		x = BitVec(reg, 32)
		a.update({reg : x})


def parseInstruc(instruct):
	if "mov" in instruct:
		instruct = "mov"
	elif "imul" in instruct:
		instruct = "mul"
	elif "idiv" in instruct:
		instruct = "div"
	return instruct

def read_x86():
	fin = file("/home/blankwall/Desktop/lopo").readlines()
	for i in fin:
		i = i.replace("[","")
		i = i.replace("]","")
		i = i.replace("dword","")
		i = i.replace("ptr","")
		i = i.replace("\n","")
		i = re.split(r'\s{2,}', i)
		if len(i) < 2:
			print "ERROR IN FORMAT: {0}".format(i)
			break
			
		if ',' in i[1]:
			k = i[1].split(",")
			k[0] = k[0].strip()
			k[1] = k[1].strip()
			i[1] = k[0]
			i.append(k[1])
		else:
			a = i[1]
			i[1] = ""
			i.append(a)
    
		i[0] = parseInstruc(i[0])
		parseReg(i[1])
		parseReg(i[2])
	
		x86.append(i) 

def mov_const(x, solver):
	if x[2].isdigit():
		a[x[1]] = int(x[2])
	else:
		a[x[1]] = a[x[2]]

def cmp_const(x, solver):
	if x[2].isdigit():
		solver.add(a[x[1]] == x[2])
	else:
		print a[x[1]], a[x[2]]
		solver.add(a[x[1]] == a[x[2]])

def add_const(x,solver):
	if x[2].isdigit():
		a[x[1]] += int(x[2])
	else:
		a[x[1]] += a[x[2]]

def sub_const(x,solver):
	if x[2].isdigit():
		a[x[1]] -= int(x[2])
	else:
		a[x[1]] -= a[x[2]]

def xchg_const(x,solver):
	a[x[1]] = a[x[2]]

def shl_const(x,solver):
	a[x[1]] = (a[x[1]] << int(x[2]))

def shr_const(x,solver):
	a[x[1]] = (a[x[1]] >> int(x[2]))

def mul_const(x,solver):
	if x[2].isdigit():
		a[x[1]] *= int(x[2])
	else:
		a[x[1]] *= a[x[2]]

def xor_const(x,solver):
	if x[2].isdigit():
		a[x[1]] = a[x[1]] ^ int(x[2])
	else:
		a[x[1]] = a[x[1]] ^ a[x[2]]

def div_const(x,solver):
	if x[2].isdigit():
		a[x[1]] = a[x[1]] / int(x[2])
	else:
		a[x[1]] = a[x[1]] / a[x[2]]

def and_const(x,solver):
	if x[2].isdigit():
		a[x[1]] = a[x[1]] & int(x[2])
	else:
		a[x[1]] = a[x[1]] & a[x[2]]

def or_const(x,solver):
	print x[2]
	if x[2].isdigit():
		a[x[1]] = a[x[1]] | int(x[2])
	else:
		a[x[1]] = a[x[1]] | a[x[2]]
	


def develop_const(x,solver):
	if x[0] == 'mov':
		mov_const(x,solver)
	elif x[0] == 'cmp':
		cmp_const(x,solver)
	elif x[0] == 'jbe':
		return
	elif x[0] == 'jle':
		return
	elif x[0] == 'jmp':
		return
	elif x[0] == 'nop':
		return
	elif x[0] == 'call':
		return
	elif x[0] == 'push':
		return
	elif x[0] == 'add':
		add_const(x,solver)
	elif x[0] == 'sub':
		sub_const(x,solver)
	elif x[0] == 'xchg':
		xchg_const(x,solver)
	elif x[0] == 'shl':
		shl_const(x,solver)
	elif x[0] == 'shr':
		shr_const(x,solver)
	elif x[0] == 'xor':
		xor_const(x,solver)
	elif x[0] == 'lea':
		mov_const(x,solver)
	elif x[0] == 'mul':
		mul_const(x,solver)
	elif x[0] == 'div':
		div_const(x,solver)
	elif x[0] == 'and':
		and_const(x,solver)
	elif x[0] == 'or':
		or_const(x,solver)
	else:
		print "UNSUPPORTED OPERATION {0}".format(x[0])

def main():
	s = Solver()
	read_x86()

	x86 = prePass()

	for i in x86:
		develop_const(i,s)

	sol = file("/home/blankwall/Desktop/polo", "wb") 
	if debug:
		for i in x86:
			sol.write(str(i) + "\n")
	
	sol.write(str(s) + "\n")
	a = str(s.check()) 
	if a == "sat":
		print s.model()
		sol.write(str(s.model()) + "\n")
		return 0
	else:
		return 0
	
main()
