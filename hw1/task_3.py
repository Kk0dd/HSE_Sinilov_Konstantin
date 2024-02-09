# Запрос у пользователя числа от 1 до 9
user_number = input("Введите число от 1 до 9: ")

# Проверка, что введены только цифры и число находится в диапазоне от 1 до 9
if user_number.isdigit() and 1 <= int(user_number) <= 9:

    # Приведение введенных данных к целому числу
    n = int(user_number)

    # Рассчет nn и nnn
    nn = int(user_number * 2)
    nnn = int(user_number * 3)

    # Рассчет суммы
    total_sum = n + nn + nnn

    # Вывод результата
    print(f"Сумма {user_number} + {nn} + {nnn} = {total_sum}")
else:
    print("Ошибка! Введите число от 1 до 9.")
