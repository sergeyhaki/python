# -*- coding: utf-8 -*-
import os
import re

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
for linetopics in atopics:
	print linetopics

	#создание папки
	folder = re.sub('\n|"|\?|:|/|\.','_', linetopics)
	folder = latinizator(folder, legend)
	print folder
	if not os.path.exists (folder):
		os.makedirs (folder)

os.system ("pause")



