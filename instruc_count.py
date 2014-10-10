import subprocess
import sys
import commands
import string

charset = '_'+string.digits+'abcdef'+'CTF{}'


initpasswd = ''
i = len(initpasswd)

while len(initpasswd) != 37:
    basepasswd = initpasswd + "_"*(37-len(initpasswd))
    basecount = 0

    result = dict()
    for c in charset:

        passwd = basepasswd[:i] + c + basepasswd[i+1:]

	cmd = "/home/blankwall/pin/pin -t /home/blankwall/pin/source/tools/ManualExamples/obj-ia32/inscount0.so  -- /home/blankwall/Desktop/reverse400 <<< %s; cat inscount.out" %(passwd)


	p = subprocess.Popen(["/bin/bash", "-c",cmd], stdout=subprocess.PIPE)
	out = p.communicate()
	
	print out
	if "YES" in out[0]:
		print initpasswd
		break
	try:
		x = [int(s) for s in out[0].split() if s.isdigit()][0]
	except:
		continue
	icount = x
        if basecount == 0:
            basecount = icount

        result[c] = icount

        print "%s = %d %d ins" %(passwd, icount, icount-basecount)

        #shortcut
        if icount-basecount > 900:
            initpasswd += c
            i += 1
            break


print initpasswd
