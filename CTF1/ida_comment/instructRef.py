import idc
import idautils
import idaapi

d = {}
with open("dict") as f:
    for line in f:
       (key, val) = line.split(":")
       d[key] = val

mnemonics = dict()

# For each of the segments
for seg_ea in Segments():
# For each of the defined elements
	for head in Heads(seg_ea, SegEnd(seg_ea)):
# If it's an instruction
		if isCode(GetFlags(head)):
# Get the mnemonic and increment the mnemonic count
			mnem = GetMnem(head)
			x = mnem.upper()
			if x in d:
				idc.MakeComm(mnemonics.get(head, head),d[x])
			
