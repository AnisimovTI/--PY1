list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0
max_number = list_numbers[max_index]

for i, current_number in enumerate(list_numbers):  # перебераем пары индекс - значение
    max_number = list_numbers[max_index]
    if current_number >= max_number:  # если текущий элемент больше того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального элемента
        max_number = list_numbers[max_index]  # и перезаписываем элемент
# получаем 9 по порядку элемент (учитывая 0)

list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]

print(list_numbers)
