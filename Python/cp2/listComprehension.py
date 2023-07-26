#list comprehension = [element for element in iterable]
numbers_v11 = []
for number in range(1, 11):
    numbers_v11.append(number)
print(numbers_v11)

numbers_v12 = [number for number in range(1, 11)]
print(numbers_v12)

#list comprehension
numbers_v31 = []
for number in range(1, 11):
    numbers_v31.append(number * 2)
print(numbers_v31)

numbers_v32 = [number * 2 for number in range(1, 11)]
print(numbers_v32)

#list comprehension con condición = [element for element in iterable if condition]
numbers_v41 = []
for number in range(1, 11):
    if number % 2 == 0:
        numbers_v41.append(number * 2)
print(numbers_v41)

numbers_v42 = [number * 2 for number in range(1, 11) if number % 2 == 0]
print(numbers_v42)
