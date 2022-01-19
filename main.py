while True:
    what = input("Выбери операцию '+' '-' '*' '/': ")
    if what not in ('+' '-' '*' '/'):
        continue
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
    elif what == "/" and b != 0:
        c = a / b
        print("Равно: " + str(c))
    else:
        print("Деление на 0!")
