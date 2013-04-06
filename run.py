import train
import random

data = [line.strip() for line in open("data/data.txt")]

Unigram, Bigram, Trigram, Fourgram, Fivegram = train.train(data)

def getNextWord(dis):
	p = random.random()
	s = 0.0
	for item in dis:
		s+=item[1]
		if s>=p:
			return item[0]
#	return dis[-1][0]

def generateOneSentence():
	i=0
	w = []
	word=getNextWord(Unigram)
	while word!='<end>':
		w.append(word)
		back = True
		dis = []
		if i >=3:
			back = False
			item = "#".join([w[i-3],w[i-2],w[i-1],w[i]])
			if item in Fivegram:
				dis=Fivegram[item]
				back = False
			else:
				back = True
		if i>=2 and back:
			back = False
			item = "#".join([w[i-2],w[i-1],w[i]])
			if item in Fourgram:
				dis=Fourgram[item]
			else:
				back = True
		if i>=1 and back:
			back = False
			item = "#".join([w[i-1], w[i]])
			if item in Trigram:
				dis = Trigram[item]
			else:
				back = True
		if back:
			back=False
			item = w[i]
			if item in Bigram:
				dis = Bigram[item]
			else:
				back=True
		if dis == []:
			dis=Unigram
		word = getNextWord(dis)
#		print word
		i+=1
	sent = " ".join(w)
	return sent

def getOnePoem(para, line):
	print "===============A POEM FOR YOUR=================="
	for i in range(para):
		for j in range(line):
			print generateOneSentence()
		print ""
	print "================================================"

getOnePoem(4, 4)
