# Код определяет плавучий объект или нет


# Функция для вычисления
def archimed(m,v):
    f_mg = float(m)*9.81
    f_arch = float(v)*9.81
    if f_arch >= f_mg:
        return True
    else:
        False

# Функция main
def main():
    print('Введите массу объекта(кг) и объем погруженной части(м³)')
    inpt=input().split()
    m = int(inpt[0])
    v = int(inpt[1])
    if archimed(m,v) == True:
        print('Объект плавучий')
    else:
        print('Объект не обладает плавучастью')


if __name__ == '__main__':
    main()