# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

numbers = [1, 2, 3, 4, 5, 6, 7]
def neighbors_sum(numbers):
    neighbors_sum = []
    length = len(numbers)
    for i in range(length):
        left_neighbor = numbers[(i - 1) % length]
        right_neighbor = numbers[(i + 1) % length]
        neighbors_sum.append(left_neighbor + right_neighbor)

    return neighbors_sum
print(neighbors_sum(numbers))





