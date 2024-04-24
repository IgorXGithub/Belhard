# Сформатировать приветсвие 3 способами

# Первый способ.
name = input('Введите свое имя: ')
last_name = input('Введите свою фамилию: ')
city = input('Введите город проживания: ')
privetstvie = f"Здравствуйте {last_name} {name} из города {city}! "
print(privetstvie)


# Второй способ.
name = input('Введите свое имя: ')
last_name = input('Введите свою фамилию: ')
city = input('Введите город проживания: ')
privetstvie = "Здравствуйте {} {} из города {}! ".format(last_name, name, city)
print(privetstvie)


# Третий способ.
name = input('Введите свое имя: ')
last_name = input('Введите свою фамилию: ')
city = input('Введите город проживания: ')
privetstvie = "Здравствуйте %(last_name)s %(name)s из города %(city)s! " % {"last_name": last_name, "name": name, "city": city}
print(privetstvie)