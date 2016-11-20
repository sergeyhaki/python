import os
import re
import urllib
from urllib2 import urlopen
import uuid

f = open("text.txt", "w")
#ft = open("tt.txt", "w")



addr = 'http://www.cqham.ru/forum/'

jpg = 0
page = 0
ipages = 1

while page < ipages:
	page += 1
	#print page
	u = urlopen('http://www.cqham.ru/forum/showthread.php?17385-Ламповый-RX-с-преобразованием-вверх/page'+str(page))
	html = u.read()
	
	
	html = re.sub('\t','', html)
	#html = re.sub('^$','', html)
	html = re.sub('\r','', html)
		
	pattern = re.compile('.+href="javascript://" class="popupctrl">', flags = re.DOTALL)
	pagehtml = re.sub(pattern,'', html)
	
	pattern = re.compile('</a>.+', flags = re.DOTALL)
	pagehtml = re.sub(pattern,'', pagehtml)	
	
	pattern = re.compile('\D+ \d+ \D+ ')
	pagehtml = re.sub(pattern,'', pagehtml)	
	
	#pagehtml = re.sub('.+href="javascript://" class="popupctrl">','', html, flags = re.DOTALL)
	#pagehtml = re.sub('</a>.+','', pagehtml, flags = re.DOTALL)
	#pagehtml = re.sub('\D+ \d+ \D+ ','', pagehtml, flags = re.DOTALL)
	
	ipages = int(pagehtml)
	
	print page
	print ipages
	
	############PAGES#############
	#pattern = re.compile(r'.*<span><a href="javascript://" class="popupctrl">.*', flags = re.DOTALL)
	#pages = pattern.match(html).group(1)
	#print pages
	##############################
	
	#ft.write (pagehtml)
	
	
	
	aresult = html.split('<blockquote class="postcontent restore ">')
	aresult.pop(0)  #удалить 0 элемент списка
	
	for txt in aresult:
		txt = re.sub('&quot;','"', txt)
		txt = re.sub('&amp;','&', txt)	
	
		
		#добыть все ссылки <a href=
		atext = txt.split('<a href="')
		atext.pop(0)  #удалить 0 элемент списка
		for href in atext:			
			href  = re.sub('" id.*','', href, flags = re.DOTALL)
			href  = re.sub('<.*?>','', href, flags = re.DOTALL)
			if "http://www.cqham.ru/forum/attachment.php" in href:			
				#f.write (href)
				#f.write ("\n")
				jpg += 1
				filename = 'attachment' + str(jpg) + '.jpg'
				#скачать ссылку
				urllib.urlretrieve(href, filename)
		
		

		#txt = re.sub('\n','', txt)
		#txt = re.sub('\r','', txt)
		#txt = re.sub('<br.*>','\n', txt, flags = re.DOTALL)		
		#txt = re.sub('<\/*b>','',txt, flags = re.DOTALL)
		#txt = re.sub('<a href="(.*)".*>','',txt, flags = re.DOTALL)
		txt = re.sub('<div.+?>','',txt, flags = re.DOTALL)
		#txt = re.sub('<a href="','',txt, flags = re.DOTALL)
		#txt = re.sub('" target.*>','',txt, flags = re.DOTALL)
		txt = re.sub('<img.+?>','',txt, flags = re.DOTALL)
		txt = re.sub('<ul.+?ul>','',txt, flags = re.DOTALL)
		txt = re.sub('<li.+?li>','',txt, flags = re.DOTALL)
		txt = re.sub('<div class="postfoot">.*','', txt, flags = re.DOTALL)
		
		f.write (txt)
		f.write ("**********************************************************************")

	
