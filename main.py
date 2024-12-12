vvod_ot_polzovatelya = int(input("Введите число: "))  # Пользователь вводит число, которое нужно проверить
# Если число меньше 2, оно не является простым
if vvod_ot_polzovatelya < 2:
    print(f"{vvod_ot_polzovatelya} - не является простым числом")  # Если число меньше 2, оно не может быть простым
else:
    # Создание списка булевых значений, обозначающих простоту чисел
    spisok = [True] * (vvod_ot_polzovatelya + 1)  # Инициализируем список длиной vvod_ot_polzovatelya + 1 со значением True
    p = 2  # Начальное значение для переменной p - первое простое число
    # Алгоритм решета Эратосфена
    while p * p <= vvod_ot_polzovatelya:  # Цикл продолжается, пока квадрат p меньше или равен uvvod_ot_polzovatelya
        if spisok[p] == True:  # Если текущее число p ещё не помечено как составное
            for i in range(p * p, vvod_ot_polzovatelya + 1, p):  # Помечаем все кратные p как составные
                spisok[i] = False  # Устанавливаем False для всех кратных p
        p += 1  # Переходим к следующему числу
    # Проверка, является ли введенное число простым
    if spisok[vvod_ot_polzovatelya]:  # Если значение в списке для vvod_ot_polzovatelya True, значит число простое
        print(f"{vvod_ot_polzovatelya} - простое число")  # Вывод сообщения, что число простое
    else:
        print(f"{vvod_ot_polzovatelya} - не является простым числом")  # Вывод сообщения, что число не простое
