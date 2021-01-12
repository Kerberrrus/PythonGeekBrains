# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

inputNumber = str(input("Input any number: "))

outputValue = int(inputNumber) + int(inputNumber + inputNumber) + \
    int(inputNumber + inputNumber + inputNumber)

print(f"Output value: {outputValue}")
