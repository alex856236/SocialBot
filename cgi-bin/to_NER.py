#!D:/Python/Python36/python.exe
#!D:/Anaconda3/python.exe
#coding=utf-8

import cgi, cgitb
from module.NER import NER
import codecs, sys 
import os, re
import json
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

print('Content-Type: text/html; charset=utf8')
print("")

parameter = cgi.FieldStorage()
text = parameter.getvalue('text')

text = re.sub(r'\s', "", text)

NER = NER()
segment, pos, text_ner = NER.predict(text)
print(json.dumps({'segment': segment, 'pos': pos, 'ner': text_ner}, ensure_ascii=False))