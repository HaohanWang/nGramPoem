import operator

data = [line.strip() for line in open("data/data.txt")]

def getProbability(dic):
	s = 0.0
	for item in dic:
		s+=dic[item]
	for item in dic:
		dic[item]=float(dic[item])/s
	l = sorted(dic.iteritems(), key=operator.itemgetter(1))
	l.reverse()
	return l
def addDictionaryItem(w, dic):
	if w in dic:
		dic[w]+=1
	elif w!='<end>':
		dic[w]=1
	return dic

def addDictionaryItemWithEnd(w, dic):
	if w in dic:
		dic[w]+=1
	else:
		dic[w]=1
	return dic

def train(data):
	Unigram = {}
	Bigram = {}
	Trigram = {}
	Fourgram = {}
	Fivegram = {}
	for line in data:
		line+=" <end>"
		w=line.split()
		for i in range(len(w)):
			Unigram = addDictionaryItem(w[i], Unigram)
			if i>=1:
				item = w[i-1]
				if item in Bigram:
					Bigram[item]=addDictionaryItem(w[i], Bigram[item])
				else:
					Bigram[item]={}
					Bigram[item]=addDictionaryItem(w[i], Bigram[item])
			if i>=2:
				item = "#".join([w[i-2], w[i-1]])
				if item in Trigram:
					Trigram[item]=addDictionaryItem(w[i], Trigram[item])
				else:
					Trigram[item]={}
					Trigram[item]=addDictionaryItem(w[i], Trigram[item])
			if i>=3:
				item = "#".join([w[i-3], w[i-2], w[i-1]])
				if item in Fourgram:
					Fourgram[item]=addDictionaryItemWithEnd(w[i], Fourgram[item])
				else:
					Fourgram[item]={}
					Fourgram[item]=addDictionaryItemWithEnd(w[i], Fourgram[item])
			if i>=4:
				item = "#".join([w[i-4], w[i-3], w[i-2], w[i-1]])
				if item in Fivegram:
					Fivegram[item]=addDictionaryItemWithEnd(w[i], Fivegram[item])
				else:
					Fivegram[item]={}
					Fivegram[item]=addDictionaryItemWithEnd(w[i], Fivegram[item])
	Unigram = getProbability(Unigram)
	for item in Bigram:
		Bigram[item]=getProbability(Bigram[item])
	for item in Trigram:
		Trigram[item]=getProbability(Trigram[item])
	for item in Fourgram:
		Fourgram[item]=getProbability(Fourgram[item])
	for item in Fivegram:
		Fivegram[item]=getProbability(Fivegram[item])
	print "-------finished training---------"
	return (Unigram, Bigram, Trigram, Fourgram, Fivegram)

#model = train(data)
#print model[1]
