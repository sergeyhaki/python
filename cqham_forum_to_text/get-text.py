import os
import re

f = open("text.txt", "w")

from urllib2 import urlopen

addr = 'http://www.cqham.ru/forum/'


page = 0

while page < 10:
	page += 1
	print page
	u = urlopen('http://www.cqham.ru/forum/showthread.php?17385-Ламповый-RX-с-преобразованием-вверх/page'+str(page))
	html = u.read()
	aresult = html.split('<blockquote class="postcontent restore ">')
	aresult.pop(0)  #удалить 0 элемент списка
	
	for txt in aresult:
		txt = re.sub('&quot;','"', txt)
		txt = re.sub('\t','', txt)
		#txt = re.sub('\n','', txt)
		#txt = re.sub('\r','', txt)
		txt = re.sub('<br.*>','\n', txt, flags = re.DOTALL)
		txt = re.sub('</blockquote>.*','', txt, flags = re.DOTALL)
		txt = re.sub('<\/*b>','',txt, flags = re.DOTALL)
		#txt = re.sub('<a href="(.*)".*>','',txt, flags = re.DOTALL)
		txt = re.sub('<.*div.*>','',txt, flags = re.DOTALL)
		txt = re.sub('<a href="','',txt, flags = re.DOTALL)
		txt = re.sub('" target.*>','',txt, flags = re.DOTALL)
		txt = re.sub('<img.*>','',txt, flags = re.DOTALL)
		f.write (txt)
		f.write ("**********************************************************************")

	
