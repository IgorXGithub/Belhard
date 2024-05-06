#Дан список чисел и на вход поступает число N, необходимо сместить список на
#указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

# Первый вариант для n <= len(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7]
def move_numbers(n:int):
    if n <= len(numbers):
        move_list = numbers[-n:] + numbers[:-n]
        return move_list

print(move_numbers(4))


numbers_two = [1, 2, 3, 4, 5, 6, 7]
def run_numbers(n:int):
    for i in range(n):
        a = numbers_two.pop()
        numbers_two.insert(0, a)
    return numbers_two

print(run_numbers(2))
