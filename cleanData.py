import nltk
text = [line.strip() for line in open("data/rawdata.txt")]

punct = '!,.?";\''

filt = []
filt.append("Contact Us /")
filt.append("Bookmark Site /")
filt.append("Link To Us /")
filt.append("Terms Of Use /")
filt.append("Privacy Policy /")
filt.append("References")

for line in text:
	out = True
	if line == "":
		out = False
	for s in filt:
		if line==s:
			out = False
	if line!="" and line[0]=='-' and line[-1]=='-':
		out = False
	if line.endswith('...'):
		line=line[:-3]
	if out:
		words = nltk.word_tokenize(line)
		s=""
		for word in words:
			if word[-1] in punct:
				s+=word[:-1]+" "
			elif word not in punct:
				s+=word+" "
		print s.lower()
