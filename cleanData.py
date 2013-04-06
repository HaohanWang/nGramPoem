text = [line.strip() for line open("rawData.txt")]

filt = []
filt.append("Contact Us /")
filt.append("Bookmark Site /")
filt.append("Link To Us /")
filt.append("Terms Of Use /")
filt.append("Privacy Policy /")
filt.append("References")

for line in text:
	out = True
	if line = "":
		out = False
	for s in filt:
		if line==s:
			out = False
	if line[0]=='-' and line[-1]=='-':
		out = False
	if out:
		print line
