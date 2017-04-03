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
    forms = {}
    for i in range (len(words)):
        if words[i] not in forms:
            forms[words[i]] = 1
        else: 
            forms[words[i]] += 1
    return forms


def making_list(forms):
    with open('forms.tsv', 'w', encoding='utf-8') as f:
        output = csv.writer(f, delimiter=':')
        for key in sorted(forms.keys()):
            output.writerow([key, forms[key]])
    print("Все готово!")

        
def main():
    words = opening()
    forms = counting_words(words)
    making_list(forms)


main()
