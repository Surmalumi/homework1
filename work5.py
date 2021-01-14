# Запросите у пользователя значения выручки и издержек фирмы.

revenue = int(input(f"Введите выручку фирмы: "))
costs = int(input(f"Введите издержки фирмы: "))
profit = revenue - costs
if revenue > costs:
    print(f"Фирма получает прибыль. Рентабельность выручки составила {profit / revenue: .2f}")
    personal = int(input(f"Введите численность сотрудников: "))
    print(f'Прибыть фирмы в расчете на одного сотрудника {profit / personal: .2f}')
elif revenue == costs:
    print(f"Фирма работает в ноль.")

elif revenue < costs:
    print(f"У вас фирма работает в убыток.")




