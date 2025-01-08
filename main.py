# Главный файл проекта


# Импортируем все нужные модули
import life_zone as lz
import Archimed as arch

def main():
    user_choise = input('Выберите, что вы хотите сделать:\n'
                        '1 — Вычислить радиус обитаемой зоны звезды\n'
                        '2 — Определить: плавучий объект или нет?\n')
    if user_choise == '1':
        lz.main()
    elif user_choise == '2':
        arch.main()
    else:
        main()
if __name__ == '__main__':
    main()