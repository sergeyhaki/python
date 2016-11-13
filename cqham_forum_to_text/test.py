import os
import re

f = open("html.txt", "w")

from urllib2 import urlopen


u = urlopen('http://www.cqham.ru/forum/showthread.php?17385-Ламповый-RX-с-преобразованием-вверх')

html = u.read()
html = re.sub('\n|\t|\r','', html)
#html = re.sub(r'  ','', html)

f.write(html)

aresult = html.split('<div class="content">')

#f.write(aresult[5])


os.system ("pause")