# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Новосибирск"],
    "Франция": ["Париж", "Марсель", "Лион"],
    "США": "Нью-Йорк",
    "Китай": ["Пекин", "Шанхай", "Гуанчжоу"],
    "Италия": "Рим",
    "Испания": "Мадрид",
    "Германия": "Берлин",
    "Великобритания": "Лондон",
    "Япония": "Токио",
    "Бразилия": "Бразилиа"
}
def get_key(my_dict: dict, value: str):
    for key, val in my_dict.items():
        if isinstance(val, list):
            if value in val:
                return key
        elif val == value:
            return key
    else:
        return None

print(get_key(cities, 'Новосибирск'))