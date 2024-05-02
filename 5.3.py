# **Вывести четные числа от 2 до N по 5 в строку

# Первый вариант
N = 14
count = 0
for i in range(2, N, 2):
    print(i, end = ' ')
    count +=1
    if count == 5:
        print()
        count = 0

# Второй вариант

N = 23
for i in range(2, N, 2):
    if i % 10 == 0:
        print(i, end= ' ')
        print()
    else:
        print(i, end= ' ')
