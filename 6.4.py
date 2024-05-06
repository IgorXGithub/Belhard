#Дан список содержащий в себе различные типы данных, отфильтровать таким
#образом, чтобы остались только строки, использование дополнительного списка
#незаконно

my_list = [1, "sort", 3.5, "quin", True]
strings_only = filter(lambda x: isinstance(x, str), my_list)
print(list(strings_only))
