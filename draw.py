import random

def draw():
    check = 0  # Проверка вводимых данных
    while check == 0:
        N = input('\nВведите количество бачонков: ')
        if N.isdigit() == False or int(N) <= 0:
            print('Пожалуйста, используйте только целые числа больше нуля!')
            print('Попробуйте еще раз!')
        else:
            N = int(N)
            numbers = list(range(1,N+1))
            check = 1

    while len(numbers) != 0:
        q = input('\nДостать бочонок? Нажмите Enter, либо n - чтобы завершить программу!\nВаш выбор: ')
        if q == 'n':
            print('\nПрограмма завершена!')
            return None
        else:
            n = random.choice(numbers)  # Выбор бочонка
            print(f'Выпал бочонок под номером {n}!')
            numbers.remove(n)  # Исключение уже выпавших бочонков из ряда выбора
    print('\nПрограмма завершена!')

if __name__ == "__main__":
    draw()
