from math import pow

while True:
    try:
        number = int(input("Введите целое число: "))
    except ValueError:
        print('Неверный ввод! Необходимо ввести целое число')
    else:
        print(pow(number, 2))
        break