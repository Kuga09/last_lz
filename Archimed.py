# Код определяет плавучий объект или нет


# Функция для вычисления
def archimed(m,v):
    f_mg = float(m)*9.81
    f_arch = float(v)*9.81
    if f_arch > f_mg:
        return 1
    elif f_arch < f_mg:
        return 0
    else:
        return 2

# Функция main
def main():
    print('Введите массу объекта(кг), объем погруженной части(м³) и плотность объекта(кг/м³)')
    inpt=input().split()
    m = int(inpt[0])
    v = int(inpt[1])
    if archimed(m,v) == 1:
        print('Объект плавучий')
    elif archimed(m,v) == 0:
        print('Объект не обладает плавучестью')
    else:
        print('Объект обладает частичной плавучестью')


if __name__ == '__main__':
    main()