import random


def get_unique_list_numbers() -> list[int]:

    random_numbers = []
    while len(random_numbers) < 15:
        number = random.randint(-10, 10)

        if number not in random_numbers:
            random_numbers.append(number)

    return random_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
  #last_string