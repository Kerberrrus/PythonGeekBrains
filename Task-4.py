# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

inputNumber = int(input("Enter the number: "))
1
# counter . if input value is 0, i will be the same.
i = 0

# cycle to get rid of digits one by one
while (inputNumber > 0):
    # take last number and compare it with previous one
    numberToCheck = inputNumber % 10
    if numberToCheck > i:
        i = numberToCheck

    inputNumber = inputNumber // 10


print(f"The highest digit is {i}")
