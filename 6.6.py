# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные


numbers = [1, 2, 3, 4, 5, 6, 7]

def sort_list(spisok: list):
    nechet_list = filter(lambda x: x % 2, spisok)
    chet_list = filter(lambda x: not x % 2, spisok)
    result_list = list(chet_list) + list(nechet_list)
    return  result_list

print(sort_list(numbers))