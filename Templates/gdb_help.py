import subprocess
import string

def backquotes(cmdwords):
        output = subprocess.Popen(cmdwords, stdout=subprocess.PIPE).communicate()[0]
        return output.strip()

def pid(program):
	pids = backquotes(['pgrep', program]).decode('utf-8')
	print(pids)

def command(program):
	print(backquotes(program).decode('utf-8'))
