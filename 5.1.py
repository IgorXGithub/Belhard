# Вывести первые N чисел кратные M и больше K

# Первый вариант
N = int(input("введите целое положительное N: "))
K = int(input("введите K: "))
M = int(input("введите M: "))
spisok_of_numbers = []
num = K + 1
while len(spisok_of_numbers) < N:
    if num % M == 0:
        spisok_of_numbers.append(num)
    num += 1
print(spisok_of_numbers)

# Второй вариант
N = int(input("введите целое положительное N: "))
K = int(input("введите K: "))
M = int(input("введите M: "))
spisok_of_numbers = [number for number in range(K + 1, K + N * M) if number % M == 0]
print(spisok_of_numbers[: N])
