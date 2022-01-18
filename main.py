action = input("Что делаем? (+, -): ")
a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

if action == "+":
    c = a + b
    print("Результат: " + str(c))
elif action == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("Неверная операция")

