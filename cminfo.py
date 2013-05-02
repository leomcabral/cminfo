#! /usr/bin/python

import urllib
from lxml import html
from datetime import datetime

url = "http://192.168.100.1/RgSignal.asp"
page = html.fromstring(urllib.urlopen(url).read())

def withValue(text):
    return text != None and ("\r\n" not in text) and (u'\xa0' not in text)

vals = [td.text for td in page.xpath("//td") if withValue(td.text)]

description = [x for idx, x in enumerate(vals) if idx % 2 == 0]
value = [x for idx, x in enumerate(vals) if idx % 2 != 0]

#v = zip(description, value)

f = open('/home/leomcabrall/github/cminfo/analisys.txt', 'a')
tamanho = len(value)
print tamanho
f.write("\n" + datetime.today().strftime('%d/%m/%Y - %H:%M:%S,'))
for idx, t in enumerate(value):
    if idx < tamanho-1:
        f.write(t + ',')
    else:
        f.write(t)

f.close()

