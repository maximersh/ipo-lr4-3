vvod_ot_polzovatelya = int(input("Введите число: "))  # Запрос ввода числа у пользователя

if vvod_ot_polzovatelya < 2:  # Проверка, если введенное число меньше 2 (такие числа не являются простыми)
    print(f"{vvod_ot_polzovatelya} - не является простым числом")  # Вывод сообщения, что число не простое
else:
    is_prost = True  # Предполагаем, что число простое
    for i in range(2, vvod_ot_polzovatelya):  # Проходим через все числа от 2 до введенного числа
        if vvod_ot_polzovatelya % i == 0:  # Если найден делитель, то число не простое
            is_prost = False
            break
    if is_prost:
        print(f"{vvod_ot_polzovatelya} - простое число")  # Вывод сообщения, что число простое
    else:
        print(f"{vvod_ot_polzovatelya} - не является простым числом")  # Вывод сообщения, что число не простое
