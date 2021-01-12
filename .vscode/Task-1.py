# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

integerA = int(
    input("Please type any number | Пожалуйста, введите любое число: "))

stringA = str(
    input("And now any string | A теперь любую строку: ")
)

if integerA == 0 or integerA == 1:
    print(
        f"Вы ввели число {integerA}. Это не только число, но и значение {bool(integerA)}.\nТакже вы ввели строку '{stringA}'")

else:
    print(f"Вы ввели число {integerA}.\nТакже вы ввели строку '{stringA}''.")
