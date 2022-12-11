import random
from string import ascii_letters, digits  # подключаем стандартный модуль string...конатенация констант


def generate_password(n: int) -> list[int]:
    possible_letters_in_password = ascii_letters + digits
    return "".join(random.sample(possible_letters_in_password, n))


generated_password = generate_password(8)
print(generated_password)
  #last_string