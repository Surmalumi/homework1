# Спортсмен занимается ежедневными пробежками.

run_1 = int(input(f"Введите сколько спортсмен пробежал в первый день, в км: "))
run_2 = int(input(f"Введите сколько спортсмен хочет пробежать км в день: "))

sport_day = 1
total_km = run_1

while total_km < run_2:
    total_km = total_km + (0.1 * total_km)
    sport_day += 1
    print(total_km)
print(f"Вы достигнете требуемых показателей на %.d день" % sport_day)

