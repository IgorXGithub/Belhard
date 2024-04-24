# Среднее арифметическое 3 чисел

first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
third_number = input('Введите третье число: ')
arithmetic_mean = (float(first_number) + float(second_number) + float(third_number)) / 3
print(round(arithmetic_mean, 3))