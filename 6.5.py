# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

numbers = [1, 2, 3, 4, 5, 6, 7]

def reverse_list(spisok: list):
    for i in range(len(spisok)):
        a = spisok.pop()
        spisok.insert(i, a)
    return spisok

print(reverse_list(numbers))
