def eratosfen_sieve(n):  # Определение функции для реализации алгоритма решета Эратосфена
    sieve = [True] * (n + 1)  # Создание списка булевых значений для всех чисел от 0 до n
    p = 2  # Начальная переменная для итерации, начинаем с первого простого числа
    while (p * p <= n):  # Цикл продолжается, пока квадрат p меньше или равен n
        if (sieve[p] == True):  # Если текущее число p ещё не помечено как составное
            for i in range(p * p, n + 1, p):  # Помечаем все кратные p как составные
                sieve[i] = False  # Устанавливаем False для всех кратных p
        p += 1  # Переходим к следующему числу
    primes = [p for p in range(2, n + 1) if sieve[p]]  # Генерируем список простых чисел
    return primes  # Возвращаем список простых чисел

user_input = int(input("Введите число: "))  # Запрос ввода числа у пользователя

if user_input < 2:  # Проверка, если введенное число меньше 2 (такие числа не являются простыми)
    print(f"{user_input} - не является простым числом")  # Вывод сообщения, что число не простое
else:
    primes = eratosfen_sieve(user_input)  # Вызов функции решета Эратосфена для нахождения простых чисел
    if user_input in primes:  # Проверка, является ли введенное число простым
        print(f"{user_input} - простое число")  # Вывод сообщения, что число простое
    else:
        print(f"{user_input} - не является простым числом")  # Вывод сообщения, что число не простое
