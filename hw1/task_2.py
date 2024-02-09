# Запрос времени у пользователя в секундах
input_seconds = input ("Введите время в секундах: ")

# Проверка ввода только чисел
if input_seconds.isdigit():

    # Приведение данных к целому числу
    total_seconds = int(input_seconds)

    # Расчет часов, минут и секунд
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Вывод результата
    print("Часы: ", hours)
    print("Минуты", minutes)
    print("Секунды", seconds)
else:
    print("Ошибка! Введите только целое число.")