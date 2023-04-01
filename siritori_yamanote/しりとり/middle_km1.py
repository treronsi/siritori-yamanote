import random
import re
import copy
import csv

f = open('dazai_akutagawa_noun.csv', encoding='utf-8-sig')
num =f.read().split()
f.close()
head = []
tail = []
for a in num:
    head.append(a[0])
    tail.append(a[-1])
#print('num:{}'.format(num[:4]))
#print('head:{}'.format(head[:4]))
#print('数:{}'.format(tail[:4]))

list_nihon = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス',
 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ',
 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ',
 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ヤ', 'ユ', 'ヨ', 'ワ']

def middle():
    fin = 0
    f = random.choice(list_nihon)
    print(str(f) + "からはじめてね")


    def siritori_part():
        global fin
        global d
        dine = 0
        draw = 0
        while dine <= 0:
            dime = random.choice(num)
            B = list(dime)
            if(dime.startswith(WORD[-1]) == True and B[-1] !="ン"):#存在するとき
                print(dime)
                d =B[-1]
                dine += 1
                used_word.append(word)
                used_word.append(dime)
                print(used_word)
                print("次は"+ str(d) + "だよ")
                num.remove(dime)
            #elif dime.startswith(word[0]) != B[-1]:
            #    print('もいっかい')
             #   dine += 1
            elif draw ==50000:#存在しない　（限りなく存在しない）とき
                print("負けました")
                dine += 1# 探索の終了
                fin += 1#ゲームの終了
            else:#未だ探索中のとき
                dine += 0
                draw += 1#もう一度繰り返す

    def shori():
        if word in used_word:
                   print('その単語もうつかったよ')
        elif word == "ギブ":
            print('降参ね')
            print("また遊ぼうね！")
            quit()#ゲームの終了
        elif N =="ン":#最後がンの場合の対応
            print("ンが付いたのでおわり！")
            print("また遊ぼうね！")
            quit()#ゲームの終了
        else:
            siritori_part()


    used_word =[]
    while fin <= 0:
        word =input("カタカナで入力してね")
        WORD = list(word)
        D = WORD[0]
        N = WORD[-1]
        if N == "ョ":
            WORD[-1] = "ヨ"
            shori()
        elif N == "ァ":
            WORD[-1] = "ア"
            shori()
        elif N == "ィ":
            WORD[-1] = "イ"
            shori()
        elif N == "ゥ":
            WORD[-1] = "ウ"
            shori()
        elif N == "ェ":
            WORD[-1] = "エ"
            shori()
        elif N == "ォ":
            WORD[-1] = "オ"
            shori()
        elif N == "ャ":
            WORD[-1] = "ヤ"
            shori()
        elif N == "ュ":
            WORD[-1] = "ユ"
            shori()
        elif N == "ッ":
            WORD[-1] = "ツ"
            shori()
        elif N == "ー":
            print("のばしぼうはやめてね、もう一回")
        else:
            shori()