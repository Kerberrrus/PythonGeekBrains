# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

inputVirychka = int(input("Введите значение вашей выручки: "))
inputIzderzki = int(input("Введине значение ваших издержек: "))

Saldo = inputVirychka - inputIzderzki

if Saldo < 0:
    print(f"У фирмы убыток {-Saldo}")
else:
    print(f"Поздравляем. У фирмы прибыль {Saldo}")
    inputNumOfWorkers = int(input(
        "Введите количество рабочих, чтобы просчитать прибыль фирмы в расчете на 1 сотрудника: "))
    print(
        f"Прибыль фирмы в расчете на 1 сотрудника: {int(Saldo/inputNumOfWorkers)}")
