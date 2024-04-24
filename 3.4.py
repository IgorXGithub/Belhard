# Подсчет отрицательных чисел

first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
third_number = input('Введите третье число: ')
spisok_of_numbers = first_number + second_number + third_number
quantity_negative_numbers = spisok_of_numbers.count('-')
print("Количество отрицательных чисел равно:", quantity_negative_numbers)