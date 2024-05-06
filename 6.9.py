# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users_data = {
    1: {'name': 'Иван', 'surname': 'Иванов', 'phone': '123-456-789', 'email': 'ivan@example.com'},
    2: {'name': 'Петр', 'surname': 'Петров', 'phone': '987-654-321', 'email': 'petr@example.com'},
    3: {'name': 'Мария', 'surname': 'Сидорова', 'phone': '111-222-333', 'email': 'maria@example.com'},
    4: {'name': 'Елена', 'surname': 'Павлова', 'phone': '555-666-777', 'email': ''},
    5: {'name': 'Алексей', 'surname': 'Смирнов', 'phone': '999-888-777'},
    6: {'name': 'Ольга', 'surname': 'Иванова', 'phone': '444-555-666', 'email': 'olga@example.com'},
    7: {'name': 'Николай', 'surname': 'Кузнецов', 'phone': '333-222-111', 'email': 'nick@example.com'},
    8: {'name': 'Татьяна', 'surname': 'Федорова', 'phone': '777-888-999', 'email': ''},
    9: {'name': 'Сергей', 'surname': 'Морозов', 'phone': '666-555-444'},
    10: {'name': 'Евгения', 'surname': 'Алексеева', 'phone': '000-111-222', 'email': 'evgenia@example.com'}
}

def get_name_without_email(data: dict):
    for key, value in data.items():
        if value.get("email") == None:
            print(value["name"])
        for k, v in value.items():
            if k == "email" and value["email"] == "":
                print(value['name'])

get_name_without_email(users_data)
