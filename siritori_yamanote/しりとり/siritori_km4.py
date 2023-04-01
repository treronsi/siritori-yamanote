import random
import re
import csv
import sys
import time
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

def nyan ():
    used_cat = []
    f = open('cat.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        cat = str(input("カタカナデニュウリョク: "))
        txt_1 = 'カタカナで入力してね'
        jtalk(txt_1)
        res = ''
        while True:
            while (res.find('\n.') == -1):
                res += sock.recv(1024)
            cat=""
            for line in res.split('\n'):
                index = line.find('WORD=')
            if cat == "ギブ":
                print("コウサンデスネ　オツカレサマ")
                txt_2='こうさんですね。おつかれさま'
                jtalk(txt_2)
                fin = 1
            elif cat not in num:
                print("ソンナネコ　イナイカ　モウイッタヨ")
                txt_3='そんなネコはいないかもういったよ'
                jtalk(txt_3)
            else:
                used_cat.append(cat)
                if (len(used_cat) == 111)  :
                    print("マケチャッタ")
                    txt_4='まけちゃった'
                    jtalk(txt_4)
                    fin = 1
                    break
                else:
                    fin = 0
                    num.remove(cat)
                    cat_random = random.choice(num)
                    print(cat_random)
                    used_cat.append(cat_random)
                    print("ツギハキミダヨ")
                    txt_5='つぎはきみだよ'
                    jtalk(txt_5)
                    num.remove(cat_random)

                    # 偶数の時
                    """if (len(used_cat) == 4)  :
                        print("負けました。")
                        txt_6='まけました'
                        jtalk(txt_6)
                        fin = 1
                        break
                        else:
                         fin = 0 """
def wan():
    used_dog = []
    f = open('dog.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        dog = str(input("カタカナデニュウリョク: "))
        if dog == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_7='こうさんですねおつかれさまです'
            jtalk(txt_7)
            break
        elif dog not in num:
            print("ソンナイヌ　イナイカ　モウイッタョ")
            txt_8='そんないぬいないかもういったよ'
            jtalk(txt_8)
        else:
            used_dog.append(dog)
            num.remove(dog)
            dog_random = random.choice(num)
            used_dog.append(dog_random)
            print(dog_random)
            print("ツギハキミダヨ")
            txt_9='つぎはきみだよ'
            jtalk(txt_9)
            num.remove(dog_random)
            print(used_dog)
            print(len(used_dog))
            if (len(used_dog) == 116 )  :
                print("マケチャッタ")
                txt_a='まけちゃった'
                jtalk(txt_a)
                fin = 1
                break
            else:
                fin = 0

def tori():
    used_tori = []
    f = open('bird.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        tori = str(input("カタカナデニュウリョク: "))
        if tori == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_b='こうさんですねおつかれさまです'
            jtalk(txt_b)
            break
        elif tori not in num:
            print("ソンナトリ　イナイカ　モウイッタ")
            txt_c='そんなとりいないかもういったよ'
            jtalk(txt_c)
        else:
            used_tori.append(tori)
            num.remove(tori)
            tori_random = random.choice(num)
            used_tori.append(tori_random)
            print(tori_random)
            print("ツギハキミダヨ")
            txt_d='つぎはきみだよ'
            jtalk(txt_d)
            num.remove(tori_random)
            print(used_tori)
            print(len(used_tori))
            if (len(used_tori) == 128 )  :
                print("マケチャッタ")
                txt_e='まけちゃった'
                jtalk(txt_e)
                fin = 1
                break
            else:
                fin = 0
def fruits():
    used_fruits = []
    f = open('fruits.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        fruits = str(input("カタカナデニュウリョク: "))
        if fruits == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_f='こうさんですねおつかれさま'
            jtalk(txt_f)
            break
        elif fruits not in num:
            print("ソノクダモノハナイカモウイッタ")
            txt_g = 'そのくだものはないかもういった'
            jtalk(txt_g)
        else:
            used_fruits.append(fruits)
            num.remove(fruits)
            fruits_random = random.choice(num)
            used_fruits.append(dog_random)
            print(fruits_random)
            print("ツギハキミダヨ")
            txt_h = 'つぎはきみだよ'
            jtalk(txt_h)
            num.remove(fruits_random)
            print(used_fruits)
            print(len(used_fruits))
            if (len(used_fruits) == 44 )  :
                print("マケチャッタ")
                fin = 1
                break
            else:
                fin = 0
def jiburi():
    used_jiburi = []
    f = open('jiburi.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        jiburi = str(input("カタカナデニュウリョク: "))
        if jiburi == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_i = 'こうさんですねおつかれさま'
            jtalk(txt_i)
            break
        elif jiburi not in num:
            print("ソノエイガ　ナイ　モウイッタョ")
            txt_j = 'そのえいがないかもういったよ'
            jtalk(txt_j)
        else:
            used_jiburi.append(jiburi)
            num.remove(jiburi)
            jiburi_random = random.choice(num)
            used_jiburi.append(jiburi_random)
            print(jiburi_random)
            print("ツギハキミダヨ")
            txt_k = 'つぎはきみだよ'
            jtalk(txt_k)
            num.remove(jiburi_random)
            print(used_jiburi)
            print(len(used_jiburi))
            if (len(used_jiburi) == 24 )  :
                print("マケチャッタ")
                txt_l = 'まけちゃった'
                jtalk(txt_l)
                fin = 1
                break
            else:
                fin = 0
def pokemon ():
    used_pokemon = []
    t = time.time()
    f = open('pokemon1.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        cat = str(input("カタカナデニュウリョク: "))
        if cat == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_m = 'こうさんですねおつかれさま'
            jtalk(txt_m)
            break
        elif cat not in num:
            print("ソノポケモン　ワカラナイ")
            txt_n = 'そのぽけもんわからない'
            jtalk(txt_n)
        else:
            used_pokemon.append(pokemon)
            if (len(used_pokemon) == 803)  :
                print("マケチャッタ")
                txt_o = 'まけちゃった'
                jtalk(txt_o)
                fin = 1
                break
            else:
                fin = 0
                num.remove(pokemon)
                pokemon_random = random.choice(num)
                print(pokemon_random)
                used_pokemon.append(pokemon_random)
                print("ツギハキミダヨ")
                txt_p = 'つぎはきみだよ'
                jtalk(txt_p)
                num.remove(pokemon_random)
                print(used_pokemon)
                print(len(used_pokemon)) 
                # 偶数の時
                """if (len(used_pokemon) == 4)  :
                    print("負けました。")
                    fin = 1
                    break
                    else:
                     fin = 0 """
def city():
    used_city = []
    f = open('ibaraki_city.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        city = str(input("カタカナデニュウリョク: "))
        if city == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_q = 'こうさんですねおつかれさま'
            jtalk(txt_q)
            break
        elif city not in num:
            print("ソノマチ　ナイ　カモウイッタョ")
            txt_r = 'そのまちないかもういったよ'
            jtalk(txt_r)
        else:
            used_city.append(city)
            num.remove(city)
            city_random = random.choice(num)
            used_city.append( city_random)
            print(city_random)
            print("ツギハキミダヨ")
            txt_s = 'つぎはきみだよ'
            jtalk(txt_s)
            num.remove(city_random)
            print(used_city)
            print(len(used_city))
            if (len(used_city) == 44 )  :
                print("マケチャッタ")
                txt_t = 'まけちゃった'
                jtalk(txt_t)
                fin = 1
                break
            else:
                fin = 0
def vege():
    used_vege = []
    f = open('vege.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        dog = str(input("カタカナデニュウリョク: "))
        if dog == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_u = 'こうさんですねおつかれさま'
            jtalk(txt_u)
            break
        elif vege not in num:
            print("ソンナヤサイ　シラナイ")
            txt_v = 'そんなやさいしらない'
            jtalk(txt_v)
        else:
            used_vege.append(vege)
            num.remove(vege)
            vege_random = random.choice(num)
            used_vege.append(dog_random)
            print(vege_random)
            print("ツギハキミダヨ")
            txt_w = 'つぎはきみだよ'
            jtalk(txt_w)
            num.remove(vege_random)
            print(used_vege)
            print(len(used_vege))
            if (len(used_vege) == 82 )  :
                print("マケチャッタ")
                fin = 1
                break
            else:
                fin = 0
def pref ():
    used_pref = []
    t = time.time()
    f = open('pref_name.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        pref = str(input("カタカナデニュウリョク: "))
        if pref == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_x = 'こうさんですねおつかれさま'
            jtalk(txt_x)
            break
        elif pref not in num:
            print("ソンナケン　ナイカ　モウイッタヨ")
            txt_y = 'そんなけんないかもういったよ'
            jtalk(txt_y)
        else:
            used_pref.append(cat)
            if (len(used_pref) == 47)  :
                print("マケチャッタ")
                txt_z = 'まけちゃった'
                jtalk(txt_z)
                fin = 1
                break
            else:
                fin = 0
                num.remove(pref)
                pref_random = random.choice(num)
                print(pref_random)
                used_pref.append(pref_random)
                print("ツギハキミダヨ")
                txt_a1 = 'つぎはきみだよ'
                jtalk(txt_a1)
                num.remove(pref_random)
                print(used_pref)
                print(len(used_pref)) 
                # 偶数の時
                """if (len(used_pref) == 4)  :
                    print("負けました。")
                    fin = 1
                    break
                    else:
                     fin = 0 """
def sori():
    used_sori = []
    f = open('souri.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        sori = str(input("カタカナデニュウリョク: "))
        if sori == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            txt_a2 = 'こうさんですねおつかれさま'
            jtalk(txt_a2)
            break
        elif sori not in num:
            print("ソンナヒト　イナイカ　モウイッタ")
            txt_a3 = 'そんなひといないかもういったよ'
            jtalk(txt_a3)
        else:
            used_sori.append(sori)
            num.remove(sori)
            sori_random = random.choice(num)
            used_sori.append(dog_random)
            print(sori_random)
            print("ツギハキミダヨ")
            txt_a4 = 'つぎはきみだよ'
            jtalk(txt_a4)
            num.remove(sori_random)
            print(used_sori)
            print(len(used_sori))
            if (len(used_sori) == 64 )  :
                print("マケチャッタ")
                txt_a5 = 'まけちゃった'
                jtalk(txt_a5)
                fin = 1
                break
            else:
                fin = 0
res = ''
while True:
    while (res.find('\n.') == -1):
        res += sock.recv(1024)
thema=''
for line in res.split('\n'):
    index = line.find('THEMA=')
    print("お題を次の中から番号で選んでね")
    txt_ab = 'おだいをつぎのなかからばんごうでえらんでね'
    jtalk(txt_ab)
    print("1、ねこ、2、いぬ、3、とり、4、クダモノ5、じぶり映画、6、ぽけもん、7、茨城県の市町村、8、ヤサイ、9、都道府県名、10、総理大臣")
    txt_ad='1、ねこ、2、いぬ、3、とり、4、クダモノ5、じぶり映画、6、ぽけもん、7、茨城県の市町村、8、ヤサイ、9、都道府県名、10、総理大臣'
    jtalk(txt_ad)
    if thema == '1' or 'ねこ'
        print("ねこですね。ギブアップの時は「ギブ」といってください")#音声
        txt_ac = 'ねこですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_ac)
        print("オダイ:ネコ　オワリ:ギブ")#display
        nyan()
        res=''
    elif thema == '2' or 'いぬ':
        print("いぬですね。ギブアップの時は「ギブ」といってください")#音声
        txt_ad = 'いぬですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_ad)
        print("オダイ:イヌ　オワリ:ギブ")#display
        wan()
        res=''
    elif thema == '3' or'とり':
        print("鳥ですね。ギブアップの時は「ギブ」といってください")#音声
        txt_ae = 'とりですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_ae)
        print("オダイ:トリ　オワリ:ギブ")#display
        tori()
        res=''
    elif thema == '4' or 'くだもの':
        print("果物ですね。ギブアップの時は「ギブ」といってください")#音声
        txt_af = 'くだものですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_af)
        print("オダイ:クダモノ　オワリ:ギブ")#display
        fruits()
        res=''
    elif thema == '5' or 'じぶり'　or 'じぶりえいが':
        print("ジブリ長編映画ですね。ギブアップの時は「ギブ」といってください")#音声
        txt_ag = 'じぶりちょうへんえいがですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_ag)
        print("オダイ:ジブリ　オワリ:ギブ")#display
        jiburi()
        res=''
    elif thema == '6' or 'ぽけもん':
        print("ポケモンですね。ギブアップの時は「ギブ」といってください")#音声
        txt_ah = 'ぽけもんですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_ah)
        print("オダイ:ポケモン　オワリ:ギブ")#display
        pokemon()
        res=''
    elif thema == '7' or 'いばらきけんしちょうそん' or 'しちょうそん':
        print("茨城県市町村ですね。ギブアップの時は「ギブ」といってください")#音声
        txt_ai = 'いばらきけんしちょうそんですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_ai)
        print("オダイ:イバラキ-シチョウソン　オワリ:ギブ")#display
        city()
        res=''
    elif thema == '8' or 'やさい':
        print("野菜ですね。ギブアップの時は「ギブ」といってください") #音声
        txt_aj = 'やさいですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_aj)
        print("オダイ:ヤサイ　オワリ:ギブ")#display
        vege()
        res=''
    elif thema == '9' or 'とどうふけんめい' or 'とどうふけん':
        print("都道府県名ですね。ギブアップの時は「ギブ」といってください")#音声
        txt_ak = 'とどうふけんめいですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_ak)
        print("オダイ:トドウフケン　オワリ:ギブ")#display
        pref()
        res=''
    elif thema == '10' or 'そうり'　or 'そうりだいじん':
        print("歴代総理大臣ですね。ギブアップの時は「ギブ」といってください")#音声
        txt_al = 'れきだいそうりだいじんですねぎぶあっぷのときはぎぶといってください'
        jtalk(txt_al)
        print("オダイ:ソウリダイジン　オワリ:ギブ")#display
        sori()
        res=''
    else:
        print("そのお題では遊べないよ。ごめんね")
        txt_am = 'そのおだいではあそべないよごめんね'
        jtalk(txt_am)
        res=''
        exit()







