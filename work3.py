#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

n = int(input("Введите число n: "))
number = str(n)
sum1 = number + number
sum2 = number + number + number
addition = n + int(sum1) + int(sum2)
print(f"У вас получилось: ", addition)