from math import pow

while True:
    try:
        number = int(input("Введите целое число: "))
    except ValueError:
        print('Неверный ввод! Необходимо ввести целое число')
        decision = input('Желаете продолжить? Y/N\n')
        if decision in ['Y', 'y', 'Yes', 'yes']:
            continue
        else:
            break
    else:
        print(pow(number, 2))
        break

#Сложность возведения в степень = О(1)
#Сложность while = O(N), где N - число циклов или число ввода от пользователя
