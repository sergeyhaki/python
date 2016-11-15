import re
2	import os
3	import time
4	import sys
5	import pickle
6	
7	f = open('c:\\TEMP\\py\\1.htm')
8	
9	fout = open('c:\\TEMP\\py\\out.txt', "w")
10	
11	text = ""
12	
13	while True:	
14		line = f.readline()	
15		if len(line) == 0: 
16			break		
17		text = text+line	
18	#print text
19	
20	aresult = text.split('<blockquote class="postcontent restore ">')
21	aresult.pop(0)  #удалить 0 элемент списка
22	
23	for txt in aresult:
24		txt = re.sub('\t','', txt)
25		txt = re.sub('<br>','', txt)
26		txt = re.sub('</blockquote>.*','', txt, flags = re.DOTALL)
27		#txt = re.sub('<.*>','',txt, flags = re.DOTALL)
28		#txt = re.sub('<a href="(.*)".*>','',txt, flags = re.DOTALL)
29		txt = re.sub('<.*div.*>','',txt, flags = re.DOTALL)
30		txt = re.sub('<a href="','',txt, flags = re.DOTALL)
31		txt = re.sub('" target.*>','',txt, flags = re.DOTALL)
32		txt = re.sub('<img.*>','',txt, flags = re.DOTALL)
33		fout.write (txt)
34		fout.write ("**********************************************************************")