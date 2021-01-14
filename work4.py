# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе

number = int(input(f"Введите целое положительное число: "))
max_number = number%10
number = number//10
while number > 0:
    if number%10 > max_number:
        max_number = number%10
    number = number//10

print(max_number)
