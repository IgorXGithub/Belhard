# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int



def convert_decimal_to_binary(n):
    d = []
    if n == 0:
        return 0
    else:
        while n > 0:
            div = n % 2
            d.append(div)
            n //= 2
    sorted_string = ''.join(map(str, sorted(d, reverse=True)))
    return sorted_string

print(convert_decimal_to_binary(10))

def convert_binary_to_decimal(binary:str):
    decimal = 0
    power = len(binary) - 1
    for number in binary:
        if number == '1':
            decimal += 2 ** power
        power -= 1
    return decimal

print(convert_binary_to_decimal('0111'))

def converter(n):
    if isinstance(n, str):
        result = convert_binary_to_decimal(n)
    elif isinstance(n, int):
        result = convert_decimal_to_binary(n)
    return result
print(converter(10))


