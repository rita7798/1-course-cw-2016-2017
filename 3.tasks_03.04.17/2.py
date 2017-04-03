#coding = utf-8

import csv

def opening():
    words = []
    with open ("anna.txt", 'r', encoding='utf-8') as f:
        for line in f.read().replace('\n', ' ').split():
            words.append(line.lower())
    for i in range(len(words)):
        words[i] = words[i].strip('.,!?*()«»\'";:-')
    return words


def counting_words(words):
    forms = {words[i]: i for i in range(len(words))}
    return forms


def making_list(forms):
    with open('forms_new.tsv', 'w', encoding='utf-8') as f:
        output = csv.writer(f, delimiter=':')
        for key in sorted(forms.keys()):
            output.writerow([key, forms[key]])
    print("Все готово!")
           

##???
## нужно забить алфавит и потом сравнивать первую букву слова с алфавитом и приплюсовывать значение к ней. в итоге получится где большие числа и где нули
##def making_alphabet(words):
##    alp = {}
##    for i in range (len(words)):
##        word = words[i]
##        f_word = word[0]
##        if word not in alp:
##            alp[f_word] = 1
##        else: 
##            alp[f_word] += 1
##    return alp
##
##
##def making_list(alp):
##    with open('alphabet.tsv', 'w', encoding='utf-8') as f:
##        output = csv.writer(f, delimiter=':')
##        for key in sorted(alp.keys()):
##            output.writerow([key, alp[key]])
##    print("Все готово!")
##
##
##???

        
def main():
    words = opening()
    forms = counting_words(words)
    making_list(forms)
##    alp = making_alphabet(words)
##    making_list(alp)

main()
