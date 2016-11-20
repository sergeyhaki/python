import os
import re
import urllib
from urllib2 import urlopen

#########################################
legend = {
' ':'_',
',':'_',
'а':'a',
'б':'b',
'в':'v',
'г':'g',
'д':'d',
'е':'e',
'ё':'yo',
'ж':'zh',
'з':'z',
'и':'i',
'й':'y',
'к':'k',
'л':'l',
'м':'m',
'н':'n',
'о':'o',
'п':'p',
'р':'r',
'с':'s',
'т':'t',
'у':'u',
'ф':'f',
'х':'h',
'ц':'c',
'ч':'ch',
'ш':'sh',
'щ':'shch',
'ъ':'y',
'ы':'y',
'ь':"_",
'э':'e',
'ю':'yu',
'я':'ya',
'А':'A',
'Б':'B',
'В':'V',
'Г':'G',
'Д':'D',
'Е':'E',
'Ё':'Yo',
'Ж':'Zh',
'З':'Z',
'И':'I',
'Й':'Y',
'К':'K',
'Л':'L',
'М':'M',
'Н':'N',
'О':'O',
'П':'P',
'Р':'R',
'С':'S',
'Т':'T',
'У':'U',
'Ф':'F',
'Х':'H',
'Ц':'Ts',
'Ч':'Ch',
'Ш':'Sh',
'Щ':'Shch',
'Ъ':'Y',
'Ы':'Y',
'Ь':"_",
'Э':'E',
'Ю':'Yu',
'Я':'Ya',
}
def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter	
##########################################

addr = 'http://www.cqham.ru/forum/'
	
ft = open("topics.txt", "r")
text = ""
while True:	
	line = ft.readline()	
	if len(line) == 0: 
		break	
	text = text+line
	
#print text

atopics = text.split('\n')
atopics.pop(0)  #удалить 0 элемент списка
for line in atopics:
	
	#создание папки
	folder = re.sub('\n|"|\?|:|/|\.','_', line)
	folder = latinizator(folder, legend)
	print folder
	if not os.path.exists (folder):
		os.makedirs (folder)
		
	
	f = open(folder + "/text.txt", "w")
	fa = open(folder + "/attach.txt", "w")
	
	jpg = 0
	page = 0
	ipages = 1

	while page < 3:
		page += 1
		#print page
		u = urlopen(line + '/page'+str(page))		
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
		
		try:
			ipages = int(pagehtml)
		except ValueError:
			ipages = 1
		
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
				href  = re.sub('".*','', href, flags = re.DOTALL)
				href  = re.sub('<.*?>','', href, flags = re.DOTALL)
				if "attachment.php" in href:
					href = addr + href
					fa.write (href)
					fa.write ("\n")
					jpg += 1
					filename = folder + '/attachment' + str(jpg) + '.jpg'
					
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
	
	f.close ()
	fa.close ()
