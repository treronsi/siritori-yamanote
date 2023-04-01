import random
import re
import csv
import sys
from easy import *
from middle import *
from high import *

print("難易度を次の中から番号で選んでね")
thema = str(input("1やさしい 2普通　3難しい →"))
thema = int(thema)
if thema == 1:
    print("やさしいですね。ギブアップの時は「ギブ」といってください")
    print("また、伸ばし棒ーには、その１つ前のカタカナから始めてください")
    easy()
elif thema == 2:
    print("ふつうですね。ギブアップの時は「ギブ」といってください")
    print("また、伸ばし棒ーには、その１つ前のカタカナから始めてください")
    middle()
elif thema == 3:
    print("難しいですね。ギブアップの時は「ギブ」といってください")
    print("また、伸ばし棒ーには、その１つ前のカタカナから始めてください")
    high()
else:
    print("その難易度では遊べないよ。ごめんね")
    exit()







