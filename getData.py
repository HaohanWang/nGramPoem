from HTMLParser import HTMLParser
from urllib import urlopen
import re

class MLStripper(HTMLParser):
    def __init__(self):
	    self.reset()
            self.fed = []
    def handle_data(self, d):
	    self.fed.append(d)
    def get_data(self):
            return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


rawfinder = re.compile("class=stxt>(.*?)</td></tr>", re.DOTALL)

for i in range(1, 199):
	url = "http://www.lovepoemsandquotes.com/LovePoem"
	if i < 10:
		url=url+"0"+str(i)+".html"
	else:
		url=url+str(i)+".html"
	#print url
	f =  urlopen(url).read()
	#print f
	rawtxt = rawfinder.findall(f)[0]
	txt=strip_tags(rawtxt)
	print txt
