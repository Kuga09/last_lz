# Код вычисления радиуса обитаемой зоны звезды


# Функция для вычисления
d = lambda L:(L/3.86)**0.5

# Функция main
def main():
    L = float(input('Введите значение светимости звезды '))
    d = lambda L:(L/3.86)**0.5 # Функция для вычисления
    print('Радиус обитаемой зоны вокруг звезды:', d(L))


if __name__ == '__main__':
    main()