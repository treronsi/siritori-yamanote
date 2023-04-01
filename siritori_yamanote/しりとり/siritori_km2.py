import random
import re
import csv
import sys
from easy import *
from middle import *
from high import *
import subprocess
from datetime import datetime

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

txt1 = '難易度を次の中から番号で選んでね'
jtalk(txt1)00
thema = str(input("1やさしい 2普通　3難しい →"))
thema = int(thema)
if thema == 1:
    txt2 = 'やさしいですね。ギブアップの時はギブといってください。また、伸ばし棒ーには、その１つ前のカタカナから始めてください'
    jtalk(txt2)
elif thema == 2:
    txt3 = 'ふつうですね。ギブアップの時は「ギブ」といってください。また、伸ばし棒ーには、その１つ前のカタカナから始めてください'
    jtalk(txt3)
elif thema == 3:
    txt4 = '難しいですね。ギブアップの時は「ギブ」といってください。また、伸ばし棒ーには、その１つ前のカタカナから始めてください'
    jtalk(txt4)
else:
    txt5='その難易度では遊べないよ。ごめんね'
    jtalk(txt5)
    exit()

