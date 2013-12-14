#Written by Kevin Chung

import os
import subprocess
import tempfile
import sys
import re

if sys.platform.startswith('linux'):
    NASM = '/usr/bin/nasm'
    NDISASM = '/usr/bin/ndisasm'
elif sys.platform.startswith('win32'):
    NASM = 'nasm/nasm.exe'
    NDISASM = 'nasm/ndisasm.exe'

def delete_file(filename):
    if os.path.exists(filename):
        os.unlink(filename)

def assemble(asm, mode="elf"):
    temp = tempfile.NamedTemporaryFile(delete=False)

    linkme = tempfile.NamedTemporaryFile(delete=False)
    dir = tempfile.gettempdir()
    try:
        temp.write(asm)
        temp.close()
        linkme.close()

        link = subprocess.check_output([NASM, '-f '+mode, temp.name, '-o '+dir+'/link.o'])
        out = subprocess.check_output([NASM, temp.name, '-o '+temp.name+'.elf'])

        asm = open(temp.name+'.elf', 'rb')
        asm = asm.read()
        delete_file(temp.name+'.elf')
        delete_file(linkme.name)
        delete_file(dir+'/link.o')
        delete_file(temp.name)
        return asm
    except:
        delete_file(temp.name+'.elf')
        delete_file(linkme.name)
        delete_file(dir+'/link.o')
        delete_file(temp.name)
        return "assembly failed"


def disassemble(elf, mode=32):
    temp = tempfile.NamedTemporaryFile(delete=False)
    try:
        temp.write(elf)
        temp.close()

        asm = subprocess.check_output([NDISASM, '-b '+str(mode), temp.name])
        delete_file(temp.name)
        return asm
    except:
        delete_file(temp.name)
        return 'disassembly failed'


def hexFormat(hex):
    a = re.sub(r'([\"])',    r'\\\1', '\\x')
    return a + (a.join(a+b for a,b in zip(hex[::2],hex[1::2])))
# print disassemble('\x48\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x48\x31\xf6\x48\x31\xd2\x0f\x05', 64)
# asm = '''
# BITS 64
# main:
#     xor rax,rax
#     push rax
#     mov rdi, 0x68732f2f6e69622f
#     push rdi
#     mov al,59                 ;execve in unistd_64.h
#     mov rdi,rsp
#     xor rsi,rsi
#     xor rdx,rdx
#     syscall
# '''

# print repr(assemble(asm, "elf64"))

print disassemble('\xFF\x25\x44\xB5\x04\x08')

b = hexFormat('31ed')
print hex(b)
print disassemble(hex('31ed'))
print disassemble('\x31\xed')
# print repr(assemble(str(b), "elf32"))
