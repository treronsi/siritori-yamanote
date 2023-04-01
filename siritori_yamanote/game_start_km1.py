import random
import re
import csv
import sys
#from testsiri import *
#from yamanote3 import *
import time
import socket
import subprocess
from datetime import datetime
import xml.etree.ElementTree as ET
host = '127.0.1.1'
port = 10500

def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode())
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

res = ''
	while (res.find('\n.') == -1):
		res += sock.recv(1024)
word=""
for line in res.split('\n'):
  index = line.find('WORD=')
	if index != -1:
			line = line[index + 6 : line.find('"', index + 6)]
			if line != '[s]':
				word = word + line
	if word == 'ゲームしよう':
		txt1 ='しりとりと山手線ゲームならどっちがいいですか'
   		jtalk(txt1)
   		print('しりとり　or 山手線ゲーム')
		if word == 'しりとり':
   			#testsiri()
   			res=''
   		elif word == 'やまのてせんげーむ'　or 'やまのてせん':
   			#yamanote()
   			res=''
		else:
			txt4 = 'そのゲームでは遊べないよ。ごめんね'
			jtalk(txt4)
			res = ''
  			print("そのゲームでは遊べないよ。ごめんね")
  			exit()