# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

set_alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z'}
text = input("Введите текст:")
text_lower = text.lower()
unique_letters = set(text_lower) & set_alphabet
letter_count = {letter: text_lower.count(letter) for letter in unique_letters}
print(letter_count)
