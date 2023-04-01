import random
import re
import csv
import sys
import time

def countdown():
    t = time.time()
    print("カウントダウン開始") 
    while True:
        c = time.time()
        if c-t >= 5:
            print("後重病")
        elif c-t >=10:
            break



def nyan ():
    used_cat = []
    t = time.time()
    f = open('cat.csv', encoding='utf-8-sig')
    num =f.read().split()
    f.close()
    fin = 0
    while fin <= 0 :
        cat = str(input("カタカナデニュウリョク: "))
        if cat == "ギブ":
            print("コウサンデスネ　オツカレサマ")
            break
        elif cat not in num:
            print("ソンナネコ　イナイカ　モウイッタ")
        else:
            used_cat.append(cat)
            if (len(used_cat) == 111)  :
                print("マケチャッタ")
                fin = 1
                break
            else:
                fin = 0
                num.remove(cat)
                cat_random = random.choice(num)
                print(cat_random)
                used_cat.append(cat_random)
                print("ツギハキミダヨ")
                num.remove(cat_random)
                print(used_cat)
                print(len(used_cat)) 
                # 偶数の時
                """if (len(used_cat) == 4)  :
                    print("負けました。")
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
            break
        elif dog not in num:
            print("ソンナイヌ　イナイカ　モウイッタ")
        else:
            used_dog.append(dog)
            dog_random = random.choice(num)
            used_dog.append(dog_random)
            print(dog_random)
            print("ツギハキミダヨ")
            num.remove(dog)
            num.remove(dog_random)
            print(used_dog)
            print(len(used_dog))
            if (len(used_dog) == 116 )  :
                print("マケチャッタ")
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
            break
        elif tori not in num:
            print("ソンナトリ　イナイカ　モウイッタ")
        else:
            used_tori.append(tori)
            tori_random = random.choice(num)
            used_tori.append(tori_random)
            print(tori_random)
            print("ツギハキミダヨ")
            num.remove(tori)
            num.remove(tori_random)
            print(used_tori)
            print(len(used_tori))
            if (len(used_tori) == 128 )  :
                print("マケチャッタ")
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
            break
        elif fruits not in num:
            print("ソノクダモノ　ナイカ　モウイッタ")
        else:
            used_fruits.append(dog)
            fruits_random = random.choice(num)
            used_fruits.append(dog_random)
            print(fruits_random)
            print("ツギハキミダヨ")
            num.remove(fruits)
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
            break
        elif jiburi not in num:
            print("ソノエイガ　ナイ　モウイッタョ")
        else:
            used_jiburi.append(dog)
            jiburi_random = random.choice(num)
            used_jiburi.append(jiburi_random)
            print(jiburi_random)
            print("ツギハキミダヨ")
            num.remove(jiburi)
            num.remove(jiburi_random)
            print(used_jiburi)
            print(len(used_jiburi))
            if (len(used_jiburi) == 24 )  :
                print("マケチャッタ")
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
            break
        elif cat not in num:
            print("ソノポケモン　ワカラナイ")
        else:
            used_pokemon.append(pokemon)
            if (len(used_pokemon) == 803)  :
                print("マケチャッタ")
                fin = 1
                break
            else:
                fin = 0
                num.remove(pokemon)
                pokemon_random = random.choice(num)
                print(pokemon_random)
                used_pokemon.append(pokemon_random)
                print("ツギハキミダヨ")
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
            break
        elif city not in num:
            print("ソノマチ　ナイ　カモウイッタョ")
        else:
            used_city.append(city)
            city_random = random.choice(num)
            used_city.append( city_random)
            print(city_random)
            print("ツギハキミダヨ")
            num.remove(city)
            num.remove(city_random)
            print(used_city)
            print(len(used_city))
            if (len(used_city) == 44 )  :
                print("マケチャッタ")
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
            break
        elif vege not in num:
            print("ソンナヤサイ　シラナイ")
        else:
            used_vege.append(dog)
            vege_random = random.choice(num)
            used_vege.append(dog_random)
            print(vege_random)
            print("ツギハキミダヨ")
            num.remove(vege)
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
            break
        elif pref not in num:
            print("ソンナケン　ナイカ　モウイッタヨ")
        else:
            used_pref.append(cat)
            if (len(used_pref) == 47)  :
                print("マケチャッタ")
                fin = 1
                break
            else:
                fin = 0
                num.remove(pref)
                pref_random = random.choice(num)
                print(pref_random)
                used_pref.append(pref_random)
                print("ツギハキミダヨ")
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
            break
        elif sori not in num:
            print("ソンナヒト　イナイカ　モウイッタ")
        else:
            used_sori.append(sori)
            sori_random = random.choice(num)
            used_sori.append(dog_random)
            print(sori_random)
            print("ツギハキミダヨ")
            num.remove(sori)
            num.remove(sori_random)
            print(used_sori)
            print(len(used_sori))
            if (len(used_sori) == 64 )  :
                print("マケチャッタ")
                fin = 1
                break
            else:
                fin = 0
print("お題を次の中から番号で選んでね")
thema = str(input("1ねこ 2いぬ →"))
thema = int(thema)
if thema == 1:
    print("ねこですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:ネコ　オワリ:ギブ")#display
    nyan()
elif thema == 2:
    print("いぬですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:イヌ　オワリ:ギブ")#display
    wan()
elif thema == 3:
    print("鳥ですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:トリ　オワリ:ギブ")#display
    tori()
elif thema == 4:
    print("果物ですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:クダモノ　オワリ:ギブ")#display
    fruits()
elif thema == 5:
    print("ジブリ長編映画ですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:ジブリ　オワリ:ギブ")#display
    jiburi()
elif thema == 6:
    print("ポケモンですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:ポケモン　オワリ:ギブ")#display
    pokemon()
elif thema == 7:
    print("茨城県市町村ですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:イバラキ-シチョウソン　オワリ:ギブ")#display
    city()
elif thema == 8:
    print("野菜ですね。ギブアップの時は「ギブ」といってください") #音声
    print("オダイ:ヤサイ　オワリ:ギブ")#display
    vege()
elif thema == 9:
    print("都道府県名ですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:トドウフケン　オワリ:ギブ")#display
    pref()
elif thema == 10:
    print("歴代総理大臣ですね。ギブアップの時は「ギブ」といってください")#音声
    print("オダイ:ソウリダイジン　オワリ:ギブ")#display
    sori()
else:
    print("そのお題では遊べないよ。ごめんね")
    exit()







