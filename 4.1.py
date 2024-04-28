# Заполнить список степенями числа 2 (от 2^1 до 2^n).

n = input(' input n: ')
spisok_stepenei = [2**number for number in range(1, int(n)+1)]
print(spisok_stepenei)
