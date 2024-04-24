# first variant
message = input('Введите сообщение: ')
message_without_spaces = message.replace(' ', '-')
print('Сообщение без пробелов:', message_without_spaces)


# Second variant
message = input('Введите сообщение: ')
list_of_words = message.split(' ')
message_without_spaces = '-'.join(list_of_words)

print('Сообщение без пробелов:', message_without_spaces)