import re
import os
import time
import sys
import pickle

f = open('c:\\TEMP\\py\\1.htm')

fout = open('c:\\TEMP\\py\\out.txt', "w")

text = ""

while True:	
	line = f.readline()	
	if len(line) == 0: 
		break		
	text = text+line	
#print text

############PAGES#############
pattern =  re.compile(r'.+<a href="javascript://" class="popupctrl" id="yui-gen11">\D+ \d+ \D+ (\d+)</a>.+', flags = re.DOTALL)
pages = pattern.match(text).group(1)
print pages
##############################

aresult = text.split('<blockquote class="postcontent restore ">')
aresult.pop(0)  #удалить 0 элемент списка

for txt in aresult:
	txt = re.sub('\t','', txt)
	txt = re.sub('<br>','', txt)
	txt = re.sub('</blockquote>.*','', txt, flags = re.DOTALL)
	#txt = re.sub('<.*>','',txt, flags = re.DOTALL)
	#txt = re.sub('<a href="(.*)".*>','',txt, flags = re.DOTALL)
	txt = re.sub('<.*div.*>','',txt, flags = re.DOTALL)
	txt = re.sub('<a href="','',txt, flags = re.DOTALL)
	txt = re.sub('" target.*>','',txt, flags = re.DOTALL)
	txt = re.sub('<img.*>','',txt, flags = re.DOTALL)
	fout.write (txt)
	fout.write ("**********************************************************************")

#print aresult
#text = re.sub(r'.+<h1>','', text)
#text = re.sub(r'\s{3,}|\t','', text)
#fout.write (text)

'''

for line in aresult:	
	fout.write (line)
	fout.write ("\n")
os.system("dir")
line = f.readline()
print line
txt = f.read(f)
print txt
with open("c:\\TEMP\\py\\1.txt") as f:
	for line in f:
		print(line, end="\n")
html = "123 qwe *-/+" 
print time.strftime('%Y %m %d %H %M %S')
points = [ { 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 } ]
points.sort(key = lambda i : i['y'])
print(points)
something = input ('Input Number')
print (something + 9)
print html
#
def foo():
	pass
	
#pages = re.sub(r'\D+ \d+ \D+ ','', pattern.match(text).group(1) , flags = re.DOTALL)
'''

