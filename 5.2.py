# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

x = input("Введите первое число: ")
operator = input("Введите математический оператор: ")
y = input("Введите второе число: ")
if operator == '+':
    sum = float(x) + float(y)
    print('сумма = ', sum)
elif operator == '-':
    sub = float(x) - float(y)
    print('разность = ', sub)
elif operator == '*':
    multiplication = float(x) * float(y)
    print('произведение = ', multiplication)
elif operator == "/":
    division = float(x) / float(y)
    print('частное = ', division)
