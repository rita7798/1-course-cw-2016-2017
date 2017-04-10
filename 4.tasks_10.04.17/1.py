import os

def making_bins(name):
    name = name.replace(" ", "/")
    print(name)
    os.makedirs(name)

def main():
    name = input("Введите что-нибудь: ")
    making_bins(name)

main()
