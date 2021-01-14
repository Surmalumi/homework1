# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.

seconds = int(input(f"Введите время в секундах: "))

seconds = seconds % (24 * 3600)

hour = seconds // 3600

seconds %= 3600

minutes = seconds // 60

seconds %= 60

print("%d:%02d:%02d" % (hour, minutes, seconds))

