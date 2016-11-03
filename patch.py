import os,stat

#Run from Applications/scitools/bin/macosx/Understand.app/Contents/MacOS
a = file("Understand", "rb").read()
a = a.replace("\xE8\xE3\x41\x00\x00\x84\xC0\x74", "\x90\x90\x90\x90\x90\x90\x90\x75")
file("Understand","w+").write(a)

st = os.stat('Understand')
os.chmod('Understand', st.st_mode | stat.S_IEXEC)
