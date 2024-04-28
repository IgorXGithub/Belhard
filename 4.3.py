# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

# 1 Вариант, если надо заполнить одинаковыми значениями
n = 2
data = {
    'name': input('введите значение name: '),
    'email': input('введите значение email: ')
}
new_dict = {key: data for key in range(0, n)}
print(new_dict)

# 2 Вариант
n = 2
key_list = ['name', 'email']
new_dict = {key: {inner_key: input(f'Введите значение для ключа "{inner_key}": ') for inner_key in key_list} for key in range(0, n)}
print(new_dict)
