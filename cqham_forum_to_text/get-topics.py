import os
import re

f = open("out.txt", "w")

#from contextlib import closing
from urllib2 import urlopen
#import html5lib

addr = 'http://www.cqham.ru/forum/'

page = 57

while page > 0:
	page -= 1
	u = urlopen("http://www.cqham.ru/forum/forumdisplay.php?9-%D2%F0%E0%ED%F1%E8%E2%E5%F0%FB-%EF%F0%E8%E5%EC%ED%E8%EA%E8-%CA%C2-%D3%CA%C2&s=6d49778dbb84ef726233eeb2ec903dec/page"+str(page))
	html = u.read()
	html = re.sub(r'\n|\t|\r','', html)
	html = re.sub(r'  ','', html)
	aresult = html.split("><")
	
	for line in aresult:
		if re.match(r'a href="showthread', line):
			line = re.sub(r'a href="','', line)
			line = re.sub('&amp;s=.+','', line)
			line = re.sub('\/page.+','', line)
			line = re.sub('quot','"', line)
			line = addr + line
			print line
			f.write(line)
			f.write("\n")

os.system ("pause")