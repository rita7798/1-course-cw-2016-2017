import os

def making_bins(number):
    i = 1
    while i <= number:
        os.makedirs(str(i))
        i += 1

    q = 1
    while q <= number:
        for f in os.listdir(i):
            os.path.join("i", f)
    os.listdir(i)



def main():
    number = int(input("Введите число: "))
    making_bins(number)

main()



i+\+q и туда добавить txt
