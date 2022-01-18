what = input("Выбери операцию '+' '-' '*' '/': ")
a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))

if what == "+":
    c = a + b
    print("Равно: " + str(c))
elif what == "-":
    c = a - b
    print("Равно: " + str(c))
elif what == "*":
    c = a * b
    print("Равно: " + str(c))
elif what == "/":
    if b == int("0"):
        print("Не делю на 0")
        exit()
    c = a / b
    print("Равно: " + str(c))
else:
    print("Такого я не умею")
