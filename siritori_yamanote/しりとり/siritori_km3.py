import random
import re
import csv
import sys
from easy import *
from middle import *
from high import *
import subprocess
import socket
from datetime import datetime
import xml.etree.ElementTree as ET
host = '127.0.1.1'
port = 10500

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

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

def testsiri():

    txt1 = '難易度を次の中から番号で選んでね'
    jtalk(txt1)00
    thema = str(input("1やさしい 2普通　3難しい →"))
    txt ='1、やさしい 、2、普通、3、難しい'
    thema = int(thema)
    res = ''
    while True:
        while (res.find('\n.') == -1):
            res += sock.recv(1024)
        thema=''
        for line in res.split('\n'):
            index = line.find('WORD=')
            if thema == '1' or 'やさしい':
                txt2 = 'やさしいですね。ギブアップの時はギブといってください。また、伸ばし棒ーには、その１つ前のカタカナから始めてください'
                jtalk(txt2)
                res =''
            elif thema == '2' or 'ふつう' :
                txt3 = 'ふつうですね。ギブアップの時は「ギブ」といってください。また、伸ばし棒ーには、その１つ前のカタカナから始めてください'
                jtalk(txt3)
                res = ''
            elif thema == '3' or 'むずかしい':
                txt4 = '難しいですね。ギブアップの時は「ギブ」といってください。また、伸ばし棒ーには、その１つ前のカタカナから始めてください'
                jtalk(txt4)
                res = ''
            else:
                txt5='その難易度では遊べないよ。ごめんね'
                jtalk(txt5)
                res = ''
                exit()

