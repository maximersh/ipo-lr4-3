user_input = int(input("Введите число: "))  # Запрос ввода числа у пользователя

if user_input < 2:  # Проверка, если введенное число меньше 2 (такие числа не являются простыми)
    print(f"{user_input} - не является простым числом")  # Вывод сообщения, что число не простое
else:
    is_prost = True  # Предполагаем, что число простое
    for i in range(2, user_input):  # Проходим через все числа от 2 до введенного числа
        if user_input % i == 0:  # Если найден делитель, то число не простое
            is_prost = False
            break
    if is_prost:
        print(f"{user_input} - простое число")  # Вывод сообщения, что число простое
    else:
        print(f"{user_input} - не является простым числом")  # Вывод сообщения, что число не простое
