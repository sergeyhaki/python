import os
import re



f = open("text.txt", "w")

#from contextlib import closing
from urllib2 import urlopen
#import html5lib

addr = 'http://www.cqham.ru/forum/'

u = urlopen('http://www.cqham.ru/forum/showthread.php?17385-Ламповый-RX-с-преобразованием-вверх')

html = u.read()
html = re.sub('\n|\t|\r','', html)
#html = re.sub(r'  ','', html)


#f.write(html)

aresult = html.split('<blockquote class="postcontent restore ">')

txt = aresult[7]

txt = re.sub(r'</blockquote>.*', '', txt, flags=re.DOTALL)

f.write(txt)


os.system ("pause")