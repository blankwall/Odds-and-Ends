import os,stat

#Run from Applications/scitools/bin/macosx/Understand.app/Contents/MacOS
a = file("Understand", "rb").read()
a = a.replace("\xbb\x08\x00\x00\x00\xeb\x14", "\xbb\x01\x00\x00\x00\xeb\x14")
file("Understand_Patched","w+").write(a)

st = os.stat('Understand_Patched')
os.chmod('Understand_Patched', st.st_mode | stat.S_IEXEC)