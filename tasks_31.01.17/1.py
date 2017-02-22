#coding = utf-8

import re


def searching(fname):
    texte = []
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    texte = text.split("\n")
    words = set()
    for i in range (len(texte)-1):
        reg = r"(\«\D+-?\d?\» \(кит.)"
        res = re.findall(reg, texte[i])
        for i in range(len(res)):
            words.add(res[i])
    for word in words:
        word = word[:-6]
        print(word)


def main():
    fname = input("Введите имя файла: ") 
    searching(fname)

main()
