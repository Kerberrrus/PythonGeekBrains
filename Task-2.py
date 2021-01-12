# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

inputTimeSeconds = int(input("Введите количество секунд: "))

hour = inputTimeSeconds // 3600
minute = (inputTimeSeconds % 3600) // 60
seconds = inputTimeSeconds - (hour * 3600 + minute * 60)


# 02d for leading zero if < 10

print(f"Your time is: {hour:02d}:{minute:02d}:{seconds:02d}")
